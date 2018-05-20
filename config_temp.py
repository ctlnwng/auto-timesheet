class Shift(object):
    day = 0
    start = ""
    end = ""

    def __init__(self, day, start, end):
        self.day = day
        self.start = start
        self.end = end

def make_shift(day, start, end):
    shift = Shift(day, start, end)
    return shift

#--------------FILL-OUT-FIELDS-BELOW----------------

# myNEU credentials
username = "<username>"
password = "<password>"

# job title as it appears on your time sheet
jobTitle = "<job_title>"

# EXAMPLE SHIFT:
# exampleShift = make_shift(1, "1030", "1300")
# the above line instantiates a shift on Tuesday from 10:30 AM - 1:00 PM

# DAY OF THE WEEK VALUES
# Monday - 0
# Tuesday - 1
# Wednesday - 2
# Thursday - 3
# Friday - 4
# Saturday - 5

# declare each of your shifts here:
shift1 = make_shift(<day_of_the_week_value>, "<start_time_military>", "<end_time_military>")

# add all your shifts to this array
shifts = [shift1, shift2, ...]
