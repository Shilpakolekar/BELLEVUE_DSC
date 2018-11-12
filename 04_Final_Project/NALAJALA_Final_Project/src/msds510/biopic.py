import datetime
import sys


class Biopic:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Biopic data
        """

        if record:
            self.record = record
            self.title_value = record["title"]
            self.site_value = record["site"]
            self.country = record["country"]
            self.year_release_value = record["year_release"]
            self.box_office_amount = record["box_office"]
            self.director = record["director"]
            self.number_of_subjects = record["number_of_subjects"]
            self.subject = record["subject"]
            self.type_of_subject = record["type_of_subject"]
            self.race_known = record["race_known"]
            self.subject_race = record["subject_race"]
            self.person_of_color = record["person_of_color"]
            self.subject_sex = record["subject_sex"]
            self.lead_actor_actress = record["lead_actor_actress"]
            self.years_since_released_value = record["years_since_released"]

    def title(self):
        """
        Returns: str: The title of the biopic
        """
        return self.title_value.strip()

    def site(self):
        """
        Returns: str: The URL of the biopic on imdb
        """
        return self.site_value

    def country(self):
        """
        Returns: str: The countries biopic release in
        """
        return self.country

    def year_release(self):
        """
        Returns:int: Year of the biopic release
        """
        return int(self.year_release_value)

    def box_office(self):
        """
        Returns: float: Total box office amount of biopic
        """
        return float(self.box_office_amount)

    def director(self):
        """
        Returns: str: The full name of the director
        """
        return self.director.strip()

    def number_of_subjects(self):
        """
        Returns:int: The number of subjects that biopic based on
        """
        return int(self.number_of_subjects)

    def subject(self):
        """
        Returns: str: The main subject that biopic based on
        """
        return self.subject.strip()

    def type_of_subject(self):
        """
        Returns: str: The type of subject that biopic based on
        """
        return self.type_of_subject

    def is_race_known(self):
        """
        Returns: bool: Is race known? (True/False)
        """

        if not self.race_known.strip():
            return None
        else:
            return True if self.current == 'KNOWN' else False

    def subject_race(self):
        """
        Returns:str: The subject race of the biopic
        """
        return self.subject_race

    def person_of_color(self):
        """
        Returns: bool: color of person? (True/False)
        """
        if not self.person_of_color.strip():
            return None
        else:
            return True if self.current == '1' else False

    def lead_actor_actress(self):
        """
        Returns:str: Actress name in the biopic
        """
        return self.lead_actor_actress.strip()

    def years_since_released(self):
        """
        Returns:int: The number of years till now since biopic released
        """
        return int(self.years_since_released_value)

    def __str__(self):
        """
        Returns:str: A human-readable value for this biopic
        """
        return self.title()

    def __repr__(self):
        """
        Returns: str: String representation of object.  Useful for debugging.
        """

        return "Biopic(" + ",".join(key + "=" + val
                                     for key, val in self.record.items()
                                     if key == 'title'
                                     or key == 'site') + ")"
    def to_markdown(self, recordslist, outfile):
        """takes a list of records, formats them and prints them to an output file.
        Args:
            recordslist: list of top 10 highest box office biopics
            outfile: a file location string.
        Result:
            prints the contents to a formatted outfile.
        """
        try:
            with open(outfile, 'w') as ofile:
                for idx, rc in enumerate(recordslist):
                    biopic = Biopic(rc)
                    ofile.write('#  %d. %s\n' % (idx + 1, biopic.title()))
                    ofile.write('*  Director: %s \n' % biopic.director)
                    ofile.write('*  Year Released: %d \n' % biopic.year_release())
                    ofile.write('*  Countries Released: %s \n' % biopic.country)
                    ofile.write('*  Box Office: $%sM\n' % format(biopic.box_office(), ",.2f"))
                    ofile.write('*  Years Since Released: %d \n' % biopic.years_since_released())
                    ofile.write('*  URL: <%s>\n' % biopic.site())
        except BaseException as e:
            print("Exception in 'to_markdown' function")
            print("Error on line {}:".format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

