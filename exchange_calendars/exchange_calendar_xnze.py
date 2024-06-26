#
# Copyright 2018 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Useful source for the history of New Zealand public holidays:
# Nancy Swarbrick, 'Public holidays', Te Ara - the Encyclopedia of New Zealand
# http://www.TeAra.govt.nz/en/public-holidays/print (accessed 22 December 2019)

from datetime import time
from zoneinfo import ZoneInfo

from pandas import Timestamp
from pandas.tseries.holiday import (
    MO,
    DateOffset,
    EasterMonday,
    GoodFriday,
    Holiday,
    next_monday,
    next_monday_or_tuesday,
    previous_workday,
    weekend_to_monday,
)

from .common_holidays import anzac_day, boxing_day, christmas, new_years_day
from .exchange_calendar import HolidayCalendar, ExchangeCalendar

# Prior to 2015, Waitangi Day and Anzac Day are not "Mondayized",
# that is, if they occur on the weekend, there is no make-up.
MONDAYIZATION_START_DATE = "2015-01-01"

# Regular Holidays
# ----------------
NewYearsDay = new_years_day(observance=next_monday)

DayAfterNewYearsDay = Holiday(
    "Day after New Year's Day",
    month=1,
    day=2,
    observance=next_monday_or_tuesday,
)

WaitangiDayNonMondayized = Holiday(
    "Waitangi Day",
    month=2,
    day=6,
    end_date=MONDAYIZATION_START_DATE,
)

WaitangiDay = Holiday(
    "Waitangi Day",
    month=2,
    day=6,
    observance=weekend_to_monday,
    start_date=MONDAYIZATION_START_DATE,
)

AnzacDayNonMondayized = anzac_day(end_date=MONDAYIZATION_START_DATE)

AnzacDay = anzac_day(
    observance=weekend_to_monday,
    start_date=MONDAYIZATION_START_DATE,
)

QueensBirthday = Holiday(
    "Queen's Birthday",
    month=6,
    day=1,
    offset=DateOffset(weekday=MO(1)),
)

LabourDay = Holiday(
    "Labour Day",
    month=10,
    day=1,
    offset=DateOffset(weekday=MO(4)),
)

Christmas = christmas(observance=next_monday)

BoxingDay = boxing_day(observance=next_monday_or_tuesday)


# Early Closes
# ------------
BusinessDayPriorToChristmasDay = Holiday(
    "Business Day prior to Christmas Day",
    month=12,
    day=25,
    observance=previous_workday,
    start_date="2011-01-01",
)

BusinessDayPriorToNewYearsDay = Holiday(
    "Business Day prior to New Year's Day",
    month=1,
    day=1,
    observance=previous_workday,
    start_date="2011-01-01",
)

# Further ad-hoc holidays and closures sourced from gaps in index series
XMAS22DEC86 = Timestamp("1986-12-22")
XMAS23DEC86 = Timestamp("1986-12-23")
XMAS24DEC86 = Timestamp("1986-12-24")
XMAS29DEC86 = Timestamp("1986-12-29")
XMAS30DEC86 = Timestamp("1986-12-30")
XMAS31DEC86 = Timestamp("1986-12-31")
XMAS24DEC90 = Timestamp("1990-12-24")
XMAS31DEC90 = Timestamp("1990-12-31")
XMAS27DEC91 = Timestamp("1991-12-27")
NYDX03JAN92 = Timestamp("1992-01-03")
XMAS31DEC99 = Timestamp("1999-12-31")
QueenMourning2022 = Timestamp("2022-09-26")

# Matariki Day. Is set by Maori Lunar system which fluctuates relative to Gregorian so no set date each year.
# https://www.mbie.govt.nz/business-and-employment/employment-and-skills/employment-legislation-reviews/matariki/matariki-public-holiday/
MatarikiDayDates = {}
MatarikiDayDates["2022"] = Timestamp("2022-06-24")
MatarikiDayDates["2023"] = Timestamp("2023-07-14")
MatarikiDayDates["2024"] = Timestamp("2024-06-28")
MatarikiDayDates["2025"] = Timestamp("2025-06-20")
MatarikiDayDates["2026"] = Timestamp("2026-07-10")
MatarikiDayDates["2027"] = Timestamp("2027-06-25")
MatarikiDayDates["2028"] = Timestamp("2028-07-14")
MatarikiDayDates["2029"] = Timestamp("2029-07-06")
MatarikiDayDates["2030"] = Timestamp("2030-06-21")
MatarikiDayDates["2031"] = Timestamp("2031-07-11")
MatarikiDayDates["2032"] = Timestamp("2032-07-02")
MatarikiDayDates["2033"] = Timestamp("2033-06-24")
MatarikiDayDates["2034"] = Timestamp("2034-07-07")
MatarikiDayDates["2035"] = Timestamp("2035-06-29")
MatarikiDayDates["2036"] = Timestamp("2036-07-21")
MatarikiDayDates["2037"] = Timestamp("2037-07-10")
MatarikiDayDates["2038"] = Timestamp("2038-06-25")
MatarikiDayDates["2039"] = Timestamp("2039-07-15")
MatarikiDayDates["2040"] = Timestamp("2040-07-06")
MatarikiDayDates["2041"] = Timestamp("2041-07-19")
MatarikiDayDates["2042"] = Timestamp("2042-07-11")
MatarikiDayDates["2043"] = Timestamp("2043-07-03")
MatarikiDayDates["2044"] = Timestamp("2044-06-24")
MatarikiDayDates["2045"] = Timestamp("2045-07-07")
MatarikiDayDates["2046"] = Timestamp("2046-06-29")
MatarikiDayDates["2047"] = Timestamp("2047-07-19")
MatarikiDayDates["2048"] = Timestamp("2048-07-03")
MatarikiDayDates["2049"] = Timestamp("2049-06-25")


class XNZEExchangeCalendar(ExchangeCalendar):
    """
    Exchange calendar for the New Zealand Exchange (NZX).

    Open Time: 10:00 AM, NZ
    Close Time: 4:45 PM, NZ

    Regularly-Observed Holidays:
    - New Year's Day
    - Day after New Year's Day
    - Waitangi Day
    - Good Friday
    - Easter Monday
    - Anzac Day
    - Queen's Birthday
    - Labour Day
    - Christmas
    - Boxing Day

    Early Closes:
    - Business Day prior to Christmas Day
    - Business Day prior to New Year's Day
    """

    regular_early_close = time(12, 45)

    name = "XNZE"

    tz = ZoneInfo("Pacific/Auckland")

    open_times = ((None, time(10)),)

    close_times = ((None, time(16, 45)),)

    @property
    def regular_holidays(self):
        return HolidayCalendar(
            [
                NewYearsDay,
                DayAfterNewYearsDay,
                WaitangiDayNonMondayized,
                WaitangiDay,
                GoodFriday,
                EasterMonday,
                AnzacDayNonMondayized,
                AnzacDay,
                QueensBirthday,
                LabourDay,
                Christmas,
                BoxingDay,
            ]
        )

    # add extra ad-hoc holidays
    @property
    def adhoc_holidays(self):
        dates = [
            XMAS22DEC86,
            XMAS23DEC86,
            XMAS24DEC86,
            XMAS29DEC86,
            XMAS30DEC86,
            XMAS31DEC86,
            XMAS24DEC90,
            XMAS31DEC90,
            XMAS27DEC91,
            NYDX03JAN92,
            XMAS31DEC99,
            QueenMourning2022,
        ]
        dates += MatarikiDayDates.values()
        return dates

    @property
    def special_closes(self):
        return [
            (
                self.regular_early_close,
                HolidayCalendar(
                    [BusinessDayPriorToChristmasDay, BusinessDayPriorToNewYearsDay]
                ),
            )
        ]
