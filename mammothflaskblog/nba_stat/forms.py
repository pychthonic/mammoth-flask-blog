from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms import IntegerField
from wtforms import RadioField
from wtforms import SelectField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length


player_selectfield_choices = [
        ("", ""), ("Alex Abrines, OKC", "Alex Abrines, OKC"), ("Quincy Acy, PHO", "Quincy Acy, PHO"), ("Jaylen Adams, ATL", "Jaylen Adams, ATL"), ("Steven Adams, OKC", "Steven Adams, OKC"), ("Bam Adebayo, MIA", "Bam Adebayo, MIA"), 
        ("Deng Adel, CLE", "Deng Adel, CLE"), ("DeVaughn Akoon-Purcell, DEN", "DeVaughn Akoon-Purcell, DEN"), ("LaMarcus Aldridge, SAS", "LaMarcus Aldridge, SAS"),
        ("Rawle Alkins, CHI", "Rawle Alkins, CHI"), ("Grayson Allen, UTA", "Grayson Allen, UTA"), ("Jarrett Allen, BRK", "Jarrett Allen, BRK"), ("Kadeem Allen, NYK", "Kadeem Allen, NYK"), ("Al-Farouq Aminu, POR", "Al-Farouq Aminu, POR"),
        ("Justin Anderson, ATL", "Justin Anderson, ATL"), ("Kyle Anderson, MEM", "Kyle Anderson, MEM"), ("Ryan Anderson, TOT", "Ryan Anderson, TOT"), ("Ryan Anderson, PHO", "Ryan Anderson, PHO"), ("Ryan Anderson, MIA", "Ryan Anderson, MIA"),
        ("Ike Anigbogu, IND", "Ike Anigbogu, IND"), ("Giannis Antetokounmpo, MIL", "Giannis Antetokounmpo, MIL"), ("Kostas Antetokounmpo, DAL", "Kostas Antetokounmpo, DAL"), ("Carmelo Anthony, HOU", "Carmelo Anthony, HOU"),
        ("OG Anunoby, TOR", "OG Anunoby, TOR"), ("Ryan Arcidiacono, CHI", "Ryan Arcidiacono, CHI"), ("Trevor Ariza, TOT", "Trevor Ariza, TOT"), ("Trevor Ariza, PHO", "Trevor Ariza, PHO"), ("Trevor Ariza, WAS", "Trevor Ariza, WAS"),
        ("D.J. Augustin, ORL", "D.J. Augustin, ORL"), ("Deandre Ayton, PHO", "Deandre Ayton, PHO"), ("Dwayne Bacon, CHO", "Dwayne Bacon, CHO"), ("Marvin Bagley, SAC", "Marvin Bagley, SAC"), ("Ron Baker, TOT", "Ron Baker, TOT"),
        ("Ron Baker, NYK", "Ron Baker, NYK"), ("Ron Baker, WAS", "Ron Baker, WAS"), ("Wade Baldwin, POR", "Wade Baldwin, POR"), ("Lonzo Ball, LAL", "Lonzo Ball, LAL"), ("Mohamed Bamba, ORL", "Mohamed Bamba, ORL"), 
        ("J.J. Barea, DAL", "J.J. Barea, DAL"), ("Harrison Barnes, TOT", "Harrison Barnes, TOT"), ("Harrison Barnes, DAL", "Harrison Barnes, DAL"), ("Harrison Barnes, SAC", "Harrison Barnes, SAC"), ("Will Barton, DEN", "Will Barton, DEN"), 
        ("Keita Bates-Diop, MIN", "Keita Bates-Diop, MIN"), ("Nicolas Batum, CHO", "Nicolas Batum, CHO"), ("Jerryd Bayless, MIN", "Jerryd Bayless, MIN"), ("Aron Baynes, BOS", "Aron Baynes, BOS"), ("Kent Bazemore, ATL", "Kent Bazemore, ATL"),
        ("Bradley Beal, WAS", "Bradley Beal, WAS"), ("Malik Beasley, DEN", "Malik Beasley, DEN"), ("Michael Beasley, LAL", "Michael Beasley, LAL"), ("Marco Belinelli, SAS", "Marco Belinelli, SAS"), ("Jordan Bell, GSW", "Jordan Bell, GSW"),
        ("DeAndre' Bembry, ATL", "DeAndre' Bembry, ATL"), ("Dragan Bender, PHO", "Dragan Bender, PHO"), ("Dairis Bertans, NOP", "Dairis Bertans, NOP"), ("Davis Bertans, SAS", "Davis Bertans, SAS"), ("Patrick Beverley, LAC", "Patrick Beverley, LAC"),
        ("Khem Birch, ORL", "Khem Birch, ORL"), ("Bismack Biyombo, CHO", "Bismack Biyombo, CHO"), ("Nemanja Bjelica, SAC", "Nemanja Bjelica, SAC"), ("Antonio Blakeney, CHI", "Antonio Blakeney, CHI"), ("Eric Bledsoe, MIL", "Eric Bledsoe, MIL"),
        ("Jaron Blossomgame, CLE", "Jaron Blossomgame, CLE"), ("Bogdan Bogdanovic, SAC", "Bogdan Bogdanovic, SAC"), ("Bojan Bogdanovic, IND", "Bojan Bogdanovic, IND"), ("Andrew Bogut, GSW", "Andrew Bogut, GSW"),
        ("Jonah Bolden, PHI", "Jonah Bolden, PHI"), ("Isaac Bonga, LAL", "Isaac Bonga, LAL"), ("Devin Booker, PHO", "Devin Booker, PHO"), ("Chris Boucher, TOR", "Chris Boucher, TOR"), ("Avery Bradley, TOT", "Avery Bradley, TOT"),
        ("Avery Bradley, LAC", "Avery Bradley, LAC"), ("Avery Bradley, MEM", "Avery Bradley, MEM"), ("Tony Bradley, UTA", "Tony Bradley, UTA"), ("Corey Brewer, TOT", "Corey Brewer, TOT"), ("Corey Brewer, PHI", "Corey Brewer, PHI"),
        ("Corey Brewer, SAC", "Corey Brewer, SAC"), ("Mikal Bridges, PHO", "Mikal Bridges, PHO"), ("Miles Bridges, CHO", "Miles Bridges, CHO"), ("Isaiah Briscoe, ORL", "Isaiah Briscoe, ORL"), ("Ryan Broekhoff, DAL", "Ryan Broekhoff, DAL"),
        ("Malcolm Brogdon, MIL", "Malcolm Brogdon, MIL"), ("Dillon Brooks, MEM", "Dillon Brooks, MEM"), ("MarShon Brooks, MEM", "MarShon Brooks, MEM"), ("Bruce Brown, DET", "Bruce Brown, DET"), ("Jaylen Brown, BOS", "Jaylen Brown, BOS"),
        ("Lorenzo Brown, TOR", "Lorenzo Brown, TOR"), ("Sterling Brown, MIL", "Sterling Brown, MIL"), ("Troy Brown, WAS", "Troy Brown, WAS"), ("Jalen Brunson, DAL", "Jalen Brunson, DAL"), ("Thomas Bryant, WAS", "Thomas Bryant, WAS"),
        ("Reggie Bullock, TOT", "Reggie Bullock, TOT"), ("Reggie Bullock, DET", "Reggie Bullock, DET"), ("Reggie Bullock, LAL", "Reggie Bullock, LAL"), ("Trey Burke, TOT", "Trey Burke, TOT"), ("Trey Burke, NYK", "Trey Burke, NYK"),
        ("Trey Burke, DAL", "Trey Burke, DAL"), ("Alec Burks, TOT", "Alec Burks, TOT"), ("Alec Burks, UTA", "Alec Burks, UTA"), ("Alec Burks, CLE", "Alec Burks, CLE"), ("Alec Burks, SAC", "Alec Burks, SAC"),
        ("Deonte Burton, OKC", "Deonte Burton, OKC"), ("Jimmy Butler, TOT", "Jimmy Butler, TOT"), ("Jimmy Butler, MIN", "Jimmy Butler, MIN"), ("Jimmy Butler, PHI", "Jimmy Butler, PHI"), ("Bruno Caboclo, MEM", "Bruno Caboclo, MEM"),
        ("Jose Calderon, DET", "Jose Calderon, DET"), ("Kentavious Caldwell-Pope, LAL", "Kentavious Caldwell-Pope, LAL"), ("Isaiah Canaan, TOT", "Isaiah Canaan, TOT"), ("Isaiah Canaan, PHO", "Isaiah Canaan, PHO"),
        ("Isaiah Canaan, MIN", "Isaiah Canaan, MIN"), ("Isaiah Canaan, MIL", "Isaiah Canaan, MIL"), ("Clint Capela, HOU", "Clint Capela, HOU"), ("DeMarre Carroll, BRK", "DeMarre Carroll, BRK"), ("Jevon Carter, MEM", "Jevon Carter, MEM"),
        ("Vince Carter, ATL", "Vince Carter, ATL"), ("Wendell Carter, CHI", "Wendell Carter, CHI"), ("Michael Carter-Williams, TOT", "Michael Carter-Williams, TOT"), ("Michael Carter-Williams, HOU", "Michael Carter-Williams, HOU"),
        ("Michael Carter-Williams, ORL", "Michael Carter-Williams, ORL"), ("Alex Caruso, LAL", "Alex Caruso, LAL"), ("Omri Casspi, MEM", "Omri Casspi, MEM"), ("Willie Cauley-Stein, SAC", "Willie Cauley-Stein, SAC"),
        ("Troy Caupain, ORL", "Troy Caupain, ORL"), ("Tyler Cavanaugh, UTA", "Tyler Cavanaugh, UTA"), ("Tyson Chandler, TOT", "Tyson Chandler, TOT"), ("Tyson Chandler, PHO", "Tyson Chandler, PHO"), ("Tyson Chandler, LAL", "Tyson Chandler, LAL"),
        ("Wilson Chandler, TOT", "Wilson Chandler, TOT"), ("Wilson Chandler, PHI", "Wilson Chandler, PHI"), ("Wilson Chandler, LAC", "Wilson Chandler, LAC"), ("Joe Chealey, CHO", "Joe Chealey, CHO"), ("Chris Chiozza, HOU", "Chris Chiozza, HOU"),
        ("Marquese Chriss, TOT", "Marquese Chriss, TOT"), ("Marquese Chriss, HOU", "Marquese Chriss, HOU"), ("Marquese Chriss, CLE", "Marquese Chriss, CLE"), ("Gary Clark, HOU", "Gary Clark, HOU"), ("Ian Clark, NOP", "Ian Clark, NOP"),
        ("Jordan Clarkson, CLE", "Jordan Clarkson, CLE"), ("John Collins, ATL", "John Collins, ATL"), ("Zach Collins, POR", "Zach Collins, POR"), ("Darren Collison, IND", "Darren Collison, IND"), ("Bonzie Colson, MIL", "Bonzie Colson, MIL"),
        ("Mike Conley, MEM", "Mike Conley, MEM"), ("Pat Connaughton, MIL", "Pat Connaughton, MIL"), ("Quinn Cook, GSW", "Quinn Cook, GSW"), ("DeMarcus Cousins, GSW", "DeMarcus Cousins, GSW"), ("Robert Covington, TOT", "Robert Covington, TOT"),
        ("Robert Covington, PHI", "Robert Covington, PHI"), ("Robert Covington, MIN", "Robert Covington, MIN"), ("Allen Crabbe, BRK", "Allen Crabbe, BRK"), ("Torrey Craig, DEN", "Torrey Craig, DEN"), ("Jamal Crawford, PHO", "Jamal Crawford, PHO"),
        ("Mitch Creek, TOT", "Mitch Creek, TOT"), ("Mitch Creek, BRK", "Mitch Creek, BRK"), ("Mitch Creek, MIN", "Mitch Creek, MIN"), ("Jae Crowder, UTA", "Jae Crowder, UTA"), ("Dante Cunningham, SAS", "Dante Cunningham, SAS"),
        ("Seth Curry, POR", "Seth Curry, POR"), ("Stephen Curry, GSW", "Stephen Curry, GSW"), ("Troy Daniels, PHO", "Troy Daniels, PHO"), ("Anthony Davis, NOP", "Anthony Davis, NOP"), ("Deyonta Davis, ATL", "Deyonta Davis, ATL"),
        ("Ed Davis, BRK", "Ed Davis, BRK"), ("Tyler Davis, OKC", "Tyler Davis, OKC"), ("Dewayne Dedmon, ATL", "Dewayne Dedmon, ATL"), ("Sam Dekker, TOT", "Sam Dekker, TOT"), ("Sam Dekker, CLE", "Sam Dekker, CLE"), ("Sam Dekker, WAS", "Sam Dekker, WAS"),
        ("Angel Delgado, LAC", "Angel Delgado, LAC"), ("Matthew Dellavedova, TOT", "Matthew Dellavedova, TOT"), ("Matthew Dellavedova, MIL", "Matthew Dellavedova, MIL"), ("Matthew Dellavedova, CLE", "Matthew Dellavedova, CLE"),
        ("Luol Deng, MIN", "Luol Deng, MIN"), ("DeMar DeRozan, SAS", "DeMar DeRozan, SAS"), ("Marcus Derrickson, GSW", "Marcus Derrickson, GSW"), ("Cheick Diallo, NOP", "Cheick Diallo, NOP"), ("Hamidou Diallo, OKC", "Hamidou Diallo, OKC"),
        ("Gorgui Dieng, MIN", "Gorgui Dieng, MIN"), ("Spencer Dinwiddie, BRK", "Spencer Dinwiddie, BRK"), ("Donte DiVincenzo, MIL", "Donte DiVincenzo, MIL"), ("Luka Doncic, DAL", "Luka Doncic, DAL"), ("Tyler Dorsey, TOT", "Tyler Dorsey, TOT"),
        ("Tyler Dorsey, ATL", "Tyler Dorsey, ATL"), ("Tyler Dorsey, MEM", "Tyler Dorsey, MEM"), ("Damyean Dotson, NYK", "Damyean Dotson, NYK"), ("PJ Dozier, BOS", "PJ Dozier, BOS"), ("Goran Dragic, MIA", "Goran Dragic, MIA"),
        ("Andre Drummond, DET", "Andre Drummond, DET"), ("Jared Dudley, BRK", "Jared Dudley, BRK"), ("Kris Dunn, CHI", "Kris Dunn, CHI"), ("Kevin Durant, GSW", "Kevin Durant, GSW"), ("Trevon Duval, MIL", "Trevon Duval, MIL"),
        ("Vince Edwards, HOU", "Vince Edwards, HOU"), ("Henry Ellenson, TOT", "Henry Ellenson, TOT"), ("Henry Ellenson, DET", "Henry Ellenson, DET"), ("Henry Ellenson, NYK", "Henry Ellenson, NYK"), ("Wayne Ellington, TOT", "Wayne Ellington, TOT"),
        ("Wayne Ellington, MIA", "Wayne Ellington, MIA"), ("Wayne Ellington, DET", "Wayne Ellington, DET"), ("Joel Embiid, PHI", "Joel Embiid, PHI"), ("James Ennis, TOT", "James Ennis, TOT"), ("James Ennis, HOU", "James Ennis, HOU"),
        ("James Ennis, PHI", "James Ennis, PHI"), ("Drew Eubanks, SAS", "Drew Eubanks, SAS"), ("Jacob Evans, GSW", "Jacob Evans, GSW"), ("Jawun Evans, TOT", "Jawun Evans, TOT"), ("Jawun Evans, PHO", "Jawun Evans, PHO"), ("Jawun Evans, OKC", "Jawun Evans, OKC"),
        ("Tyreke Evans, IND", "Tyreke Evans, IND"), ("Dante Exum, UTA", "Dante Exum, UTA"), ("Kenneth Faried, TOT", "Kenneth Faried, TOT"), ("Kenneth Faried, BRK", "Kenneth Faried, BRK"), ("Kenneth Faried, HOU", "Kenneth Faried, HOU"),
        ("Derrick Favors, UTA", "Derrick Favors, UTA"), ("Cristiano Felicio, CHI", "Cristiano Felicio, CHI"), ("Raymond Felton, OKC", "Raymond Felton, OKC"), ("Terrance Ferguson, OKC", "Terrance Ferguson, OKC"), ("Yogi Ferrell, SAC", "Yogi Ferrell, SAC"),
        ("Dorian Finney-Smith, DAL", "Dorian Finney-Smith, DAL"), ("Bryn Forbes, SAS", "Bryn Forbes, SAS"), ("Evan Fournier, ORL", "Evan Fournier, ORL"), ("De'Aaron Fox, SAC", "De'Aaron Fox, SAC"), ("Melvin Frazier, ORL", "Melvin Frazier, ORL"),
        ("Tim Frazier, TOT", "Tim Frazier, TOT"), ("Tim Frazier, NOP", "Tim Frazier, NOP"), ("Tim Frazier, MIL", "Tim Frazier, MIL"), ("Jimmer Fredette, PHO", "Jimmer Fredette, PHO"), ("Channing Frye, CLE", "Channing Frye, CLE"),
        ("Markelle Fultz, PHI", "Markelle Fultz, PHI"), ("Danilo Gallinari, LAC", "Danilo Gallinari, LAC"), ("Langston Galloway, DET", "Langston Galloway, DET"), ("Billy Garrett, NYK", "Billy Garrett, NYK"), ("Marc Gasol, TOT", "Marc Gasol, TOT"),
        ("Marc Gasol, MEM", "Marc Gasol, MEM"), ("Marc Gasol, TOR", "Marc Gasol, TOR"), ("Pau Gasol, TOT", "Pau Gasol, TOT"), ("Pau Gasol, SAS", "Pau Gasol, SAS"), ("Pau Gasol, MIL", "Pau Gasol, MIL"), ("Rudy Gay, SAS", "Rudy Gay, SAS"),
        ("Paul George, OKC", "Paul George, OKC"), ("Taj Gibson, MIN", "Taj Gibson, MIN"), ("Harry Giles, SAC", "Harry Giles, SAC"), ("Shai Gilgeous-Alexander, LAC", "Shai Gilgeous-Alexander, LAC"), ("Rudy Gobert, UTA", "Rudy Gobert, UTA"),
        ("Brandon Goodwin, DEN", "Brandon Goodwin, DEN"), ("Aaron Gordon, ORL", "Aaron Gordon, ORL"), ("Eric Gordon, HOU", "Eric Gordon, HOU"), ("Marcin Gortat, LAC", "Marcin Gortat, LAC"), ("Devonte' Graham, CHO", "Devonte' Graham, CHO"),
        ("Treveon Graham, BRK", "Treveon Graham, BRK"), ("Jerami Grant, OKC", "Jerami Grant, OKC"), ("Jerian Grant, ORL", "Jerian Grant, ORL"), ("Donte Grantham, OKC", "Donte Grantham, OKC"), ("Danny Green, TOR", "Danny Green, TOR"),
        ("Draymond Green, GSW", "Draymond Green, GSW"), ("Gerald Green, HOU", "Gerald Green, HOU"), ("JaMychal Green, TOT", "JaMychal Green, TOT"), ("JaMychal Green, MEM", "JaMychal Green, MEM"), ("JaMychal Green, LAC", "JaMychal Green, LAC"),
        ("Jeff Green, WAS", "Jeff Green, WAS"), ("Blake Griffin, DET", "Blake Griffin, DET"), ("Daniel Hamilton, ATL", "Daniel Hamilton, ATL"), ("Dusty Hannahs, MEM", "Dusty Hannahs, MEM"), ("Tim Hardaway, TOT", "Tim Hardaway, TOT"),
        ("Tim Hardaway, NYK", "Tim Hardaway, NYK"), ("Tim Hardaway, DAL", "Tim Hardaway, DAL"), ("James Harden, HOU", "James Harden, HOU"), ("Maurice Harkless, POR", "Maurice Harkless, POR"), ("Montrezl Harrell, LAC", "Montrezl Harrell, LAC"),
        ("Devin Harris, DAL", "Devin Harris, DAL"), ("Gary Harris, DEN", "Gary Harris, DEN"), ("Joe Harris, BRK", "Joe Harris, BRK"), ("Tobias Harris, TOT", "Tobias Harris, TOT"), ("Tobias Harris, LAC", "Tobias Harris, LAC"),
        ("Tobias Harris, PHI", "Tobias Harris, PHI"), ("Andrew Harrison, TOT", "Andrew Harrison, TOT"), ("Andrew Harrison, MEM", "Andrew Harrison, MEM"), ("Andrew Harrison, CLE", "Andrew Harrison, CLE"), ("Andrew Harrison, NOP", "Andrew Harrison, NOP"),
        ("Shaquille Harrison, CHI", "Shaquille Harrison, CHI"), ("Josh Hart, LAL", "Josh Hart, LAL"), ("Isaiah Hartenstein, HOU", "Isaiah Hartenstein, HOU"), ("Udonis Haslem, MIA", "Udonis Haslem, MIA"), ("Gordon Hayward, BOS", "Gordon Hayward, BOS"),
        ("John Henson, MIL", "John Henson, MIL"), ("Juan Hernangomez, DEN", "Juan Hernangomez, DEN"), ("Willy Hernangomez, CHO", "Willy Hernangomez, CHO"), ("Mario Hezonja, NYK", "Mario Hezonja, NYK"), ("Isaiah Hicks, NYK", "Isaiah Hicks, NYK"),
        ("Buddy Hield, SAC", "Buddy Hield, SAC"), ("Haywood Highsmith, PHI", "Haywood Highsmith, PHI"), ("Nene Hilario, HOU", "Nene Hilario, HOU"), ("George Hill, TOT", "George Hill, TOT"), ("George Hill, CLE", "George Hill, CLE"),
        ("George Hill, MIL", "George Hill, MIL"), ("Solomon Hill, NOP", "Solomon Hill, NOP"), ("Aaron Holiday, IND", "Aaron Holiday, IND"), ("Jrue Holiday, NOP", "Jrue Holiday, NOP"), ("Justin Holiday, TOT", "Justin Holiday, TOT"),
        ("Justin Holiday, CHI", "Justin Holiday, CHI"), ("Justin Holiday, MEM", "Justin Holiday, MEM"), ("John Holland, CLE", "John Holland, CLE"), ("Rondae Hollis-Jefferson, BRK", "Rondae Hollis-Jefferson, BRK"), ("Richaun Holmes, PHO", "Richaun Holmes, PHO"),
        ("Rodney Hood, TOT", "Rodney Hood, TOT"), ("Rodney Hood, CLE", "Rodney Hood, CLE"), ("Rodney Hood, POR", "Rodney Hood, POR"), ("Al Horford, BOS", "Al Horford, BOS"), ("Danuel House, HOU", "Danuel House, HOU"), ("Dwight Howard, WAS", "Dwight Howard, WAS"),
        ("Kevin Huerter, ATL", "Kevin Huerter, ATL"), ("Isaac Humphries, ATL", "Isaac Humphries, ATL"), ("R.J. Hunter, BOS", "R.J. Hunter, BOS"), ("Chandler Hutchison, CHI", "Chandler Hutchison, CHI"), ("Serge Ibaka, TOR", "Serge Ibaka, TOR"),
        ("Andre Iguodala, GSW", "Andre Iguodala, GSW"), ("Ersan Ilyasova, MIL", "Ersan Ilyasova, MIL"), ("Joe Ingles, UTA", "Joe Ingles, UTA"), ("Andre Ingram, LAL", "Andre Ingram, LAL"), ("Brandon Ingram, LAL", "Brandon Ingram, LAL"),
        ("Kyrie Irving, BOS", "Kyrie Irving, BOS"), ("Jonathan Isaac, ORL", "Jonathan Isaac, ORL"), ("Wesley Iwundu, ORL", "Wesley Iwundu, ORL"), ("Demetrius Jackson, PHI", "Demetrius Jackson, PHI"), ("Frank Jackson, NOP", "Frank Jackson, NOP"),
        ("Jaren Jackson, MEM", "Jaren Jackson, MEM"), ("Josh Jackson, PHO", "Josh Jackson, PHO"), ("Justin Jackson, TOT", "Justin Jackson, TOT"), ("Justin Jackson, SAC", "Justin Jackson, SAC"), ("Justin Jackson, DAL", "Justin Jackson, DAL"),
        ("Reggie Jackson, DET", "Reggie Jackson, DET"), ("LeBron James, LAL", "LeBron James, LAL"), ("Amile Jefferson, ORL", "Amile Jefferson, ORL"), ("John Jenkins, TOT", "John Jenkins, TOT"), ("John Jenkins, WAS", "John Jenkins, WAS"),
        ("John Jenkins, NYK", "John Jenkins, NYK"), ("Jonas Jerebko, GSW", "Jonas Jerebko, GSW"), ("Alize Johnson, IND", "Alize Johnson, IND"), ("Amir Johnson, PHI", "Amir Johnson, PHI"), ("B.J. Johnson, TOT", "B.J. Johnson, TOT"),
        ("B.J. Johnson, ATL", "B.J. Johnson, ATL"), ("B.J. Johnson, SAC", "B.J. Johnson, SAC"), ("James Johnson, MIA", "James Johnson, MIA"), ("Stanley Johnson, TOT", "Stanley Johnson, TOT"), ("Stanley Johnson, DET", "Stanley Johnson, DET"),
        ("Stanley Johnson, NOP", "Stanley Johnson, NOP"), ("Tyler Johnson, TOT", "Tyler Johnson, TOT"), ("Tyler Johnson, MIA", "Tyler Johnson, MIA"), ("Tyler Johnson, PHO", "Tyler Johnson, PHO"), ("Wesley Johnson, TOT", "Wesley Johnson, TOT"),
        ("Wesley Johnson, NOP", "Wesley Johnson, NOP"), ("Wesley Johnson, WAS", "Wesley Johnson, WAS"), ("Nikola Jokic, DEN", "Nikola Jokic, DEN"), ("Damian Jones, GSW", "Damian Jones, GSW"), ("Derrick Jones, MIA", "Derrick Jones, MIA"),
        ("Jalen Jones, CLE", "Jalen Jones, CLE"), ("Jemerrio Jones, LAL", "Jemerrio Jones, LAL"), ("Terrence Jones, HOU", "Terrence Jones, HOU"), ("Tyus Jones, MIN", "Tyus Jones, MIN"), ("DeAndre Jordan, TOT", "DeAndre Jordan, TOT"),
        ("DeAndre Jordan, DAL", "DeAndre Jordan, DAL"), ("DeAndre Jordan, NYK", "DeAndre Jordan, NYK"), ("Cory Joseph, IND", "Cory Joseph, IND"), ("Frank Kaminsky, CHO", "Frank Kaminsky, CHO"), ("Enes Kanter, TOT", "Enes Kanter, TOT"),
        ("Enes Kanter, NYK", "Enes Kanter, NYK"), ("Enes Kanter, POR", "Enes Kanter, POR"), ("Luke Kennard, DET", "Luke Kennard, DET"), ("Michael Kidd-Gilchrist, CHO", "Michael Kidd-Gilchrist, CHO"), ("George King, PHO", "George King, PHO"),
        ("Maxi Kleber, DAL", "Maxi Kleber, DAL"), ("Brandon Knight, TOT", "Brandon Knight, TOT"), ("Brandon Knight, HOU", "Brandon Knight, HOU"), ("Brandon Knight, CLE", "Brandon Knight, CLE"), ("Kevin Knox, NYK", "Kevin Knox, NYK"),
        ("Furkan Korkmaz, PHI", "Furkan Korkmaz, PHI"), ("Luke Kornet, NYK", "Luke Kornet, NYK"), ("Kyle Korver, TOT", "Kyle Korver, TOT"), ("Kyle Korver, CLE", "Kyle Korver, CLE"), ("Kyle Korver, UTA", "Kyle Korver, UTA"),
        ("Kosta Koufos, SAC", "Kosta Koufos, SAC"), ("Rodions Kurucs, BRK", "Rodions Kurucs, BRK"), ("Kyle Kuzma, LAL", "Kyle Kuzma, LAL"), ("Skal Labissiere, TOT", "Skal Labissiere, TOT"), ("Skal Labissiere, SAC", "Skal Labissiere, SAC"),
        ("Skal Labissiere, POR", "Skal Labissiere, POR"), ("Jeremy Lamb, CHO", "Jeremy Lamb, CHO"), ("Zach LaVine, CHI", "Zach LaVine, CHI"), ("Jake Layman, POR", "Jake Layman, POR"), ("T.J. Leaf, IND", "T.J. Leaf, IND"),
        ("Courtney Lee, TOT", "Courtney Lee, TOT"), ("Courtney Lee, NYK", "Courtney Lee, NYK"), ("Courtney Lee, DAL", "Courtney Lee, DAL"), ("Damion Lee, GSW", "Damion Lee, GSW"), ("Walt Lemon, CHI", "Walt Lemon, CHI"), ("Alex Len, ATL", "Alex Len, ATL"),
        ("Kawhi Leonard, TOR", "Kawhi Leonard, TOR"), ("Meyers Leonard, POR", "Meyers Leonard, POR"), ("Jon Leuer, DET", "Jon Leuer, DET"), ("Caris LeVert, BRK", "Caris LeVert, BRK"), ("Damian Lillard, POR", "Damian Lillard, POR"),
        ("Jeremy Lin, TOT", "Jeremy Lin, TOT"), ("Jeremy Lin, ATL", "Jeremy Lin, ATL"), ("Jeremy Lin, TOR", "Jeremy Lin, TOR"), ("Shaun Livingston, GSW", "Shaun Livingston, GSW"), ("Zach Lofton, DET", "Zach Lofton, DET"),
        ("Kevon Looney, GSW", "Kevon Looney, GSW"), ("Brook Lopez, MIL", "Brook Lopez, MIL"), ("Robin Lopez, CHI", "Robin Lopez, CHI"), ("Kevin Love, CLE", "Kevin Love, CLE"), ("Kyle Lowry, TOR", "Kyle Lowry, TOR"), ("Jordan Loyd, TOR", "Jordan Loyd, TOR"),
        ("Kalin Lucas, DET", "Kalin Lucas, DET"), ("Timothe Luwawu-Cabarrot, TOT", "Timothe Luwawu-Cabarrot, TOT"), ("Timothe Luwawu-Cabarrot, OKC", "Timothe Luwawu-Cabarrot, OKC"),
        ("Timothe Luwawu-Cabarrot, CHI", "Timothe Luwawu-Cabarrot, CHI"), ("Tyler Lydon, DEN", "Tyler Lydon, DEN"), ("Trey Lyles, DEN", "Trey Lyles, DEN"), ("Scott Machado, LAL", "Scott Machado, LAL"), ("Shelvin Mack, TOT", "Shelvin Mack, TOT"),
        ("Shelvin Mack, MEM", "Shelvin Mack, MEM"), ("Shelvin Mack, CHO", "Shelvin Mack, CHO"), ("Daryl Macon, DAL", "Daryl Macon, DAL"), ("J.P. Macura, CHO", "J.P. Macura, CHO"), ("Ian Mahinmi, WAS", "Ian Mahinmi, WAS"), ("Thon Maker, TOT", "Thon Maker, TOT"),
        ("Thon Maker, MIL", "Thon Maker, MIL"), ("Thon Maker, DET", "Thon Maker, DET"), ("Boban Marjanovic, TOT", "Boban Marjanovic, TOT"), ("Boban Marjanovic, LAC", "Boban Marjanovic, LAC"), ("Boban Marjanovic, PHI", "Boban Marjanovic, PHI"),
        ("Lauri Markkanen, CHI", "Lauri Markkanen, CHI"), ("Jarell Martin, ORL", "Jarell Martin, ORL"), ("Frank Mason, SAC", "Frank Mason, SAC"), ("Yante Maten, MIA", "Yante Maten, MIA"), ("Wesley Matthews, TOT", "Wesley Matthews, TOT"),
        ("Wesley Matthews, DAL", "Wesley Matthews, DAL"), ("Wesley Matthews, NYK", "Wesley Matthews, NYK"), ("Wesley Matthews, IND", "Wesley Matthews, IND"), ("Luc Mbah a Moute, LAC", "Luc Mbah a Moute, LAC"), ("Tahjere McCall, BRK", "Tahjere McCall, BRK"),
        ("Patrick McCaw, TOT", "Patrick McCaw, TOT"), ("Patrick McCaw, CLE", "Patrick McCaw, CLE"), ("Patrick McCaw, TOR", "Patrick McCaw, TOR"), ("CJ McCollum, POR", "CJ McCollum, POR"), ("T.J. McConnell, PHI", "T.J. McConnell, PHI"),
        ("Doug McDermott, IND", "Doug McDermott, IND"), ("JaVale McGee, LAL", "JaVale McGee, LAL"), ("Rodney McGruder, MIA", "Rodney McGruder, MIA"), ("Alfonzo McKinnie, GSW", "Alfonzo McKinnie, GSW"), ("Ben McLemore, SAC", "Ben McLemore, SAC"),
        ("Jordan McRae, WAS", "Jordan McRae, WAS"), ("Jodie Meeks, TOR", "Jodie Meeks, TOR"), ("Salah Mejri, DAL", "Salah Mejri, DAL"), ("De'Anthony Melton, PHO", "De'Anthony Melton, PHO"), ("Chimezie Metu, SAS", "Chimezie Metu, SAS"),
        ("Khris Middleton, MIL", "Khris Middleton, MIL"), ("C.J. Miles, TOT", "C.J. Miles, TOT"), ("C.J. Miles, TOR", "C.J. Miles, TOR"), ("C.J. Miles, MEM", "C.J. Miles, MEM"), ("Darius Miller, NOP", "Darius Miller, NOP"), ("Malcolm Miller, TOR", "Malcolm Miller, TOR"),
        ("Patty Mills, SAS", "Patty Mills, SAS"), ("Paul Millsap, DEN", "Paul Millsap, DEN"), ("Shake Milton, PHI", "Shake Milton, PHI"), ("Nikola Mirotic, TOT", "Nikola Mirotic, TOT"), ("Nikola Mirotic, NOP", "Nikola Mirotic, NOP"),
        ("Nikola Mirotic, MIL", "Nikola Mirotic, MIL"), ("Donovan Mitchell, UTA", "Donovan Mitchell, UTA"), ("Naz Mitrou-Long, UTA", "Naz Mitrou-Long, UTA"), ("Malik Monk, CHO", "Malik Monk, CHO"), ("Greg Monroe, TOT", "Greg Monroe, TOT"),
        ("Greg Monroe, TOR", "Greg Monroe, TOR"), ("Greg Monroe, BOS", "Greg Monroe, BOS"), ("Greg Monroe, PHI", "Greg Monroe, PHI"), ("E'Twaun Moore, NOP", "E'Twaun Moore, NOP"), ("Eric Moreland, TOT", "Eric Moreland, TOT"), ("Eric Moreland, PHO", "Eric Moreland, PHO"),
        ("Eric Moreland, TOR", "Eric Moreland, TOR"), ("Jaylen Morris, MIL", "Jaylen Morris, MIL"), ("Marcus Morris, BOS", "Marcus Morris, BOS"), ("Markieff Morris, TOT", "Markieff Morris, TOT"), ("Markieff Morris, WAS", "Markieff Morris, WAS"),
        ("Markieff Morris, OKC", "Markieff Morris, OKC"), ("Monte Morris, DEN", "Monte Morris, DEN"), ("Donatas Motiejunas, SAS", "Donatas Motiejunas, SAS"), ("Johnathan Motley, LAC", "Johnathan Motley, LAC"), ("Emmanuel Mudiay, NYK", "Emmanuel Mudiay, NYK"),
        ("Jamal Murray, DEN", "Jamal Murray, DEN"), ("Dzanan Musa, BRK", "Dzanan Musa, BRK"), ("Mike Muscala, TOT", "Mike Muscala, TOT"), ("Mike Muscala, PHI", "Mike Muscala, PHI"), ("Mike Muscala, LAL", "Mike Muscala, LAL"),
        ("Sviatoslav Mykhailiuk, TOT", "Sviatoslav Mykhailiuk, TOT"), ("Sviatoslav Mykhailiuk, LAL", "Sviatoslav Mykhailiuk, LAL"), ("Sviatoslav Mykhailiuk, DET", "Sviatoslav Mykhailiuk, DET"), ("Abdel Nader, OKC", "Abdel Nader, OKC"),
        ("Larry Nance, CLE", "Larry Nance, CLE"), ("Shabazz Napier, BRK", "Shabazz Napier, BRK"), ("Raul Neto, UTA", "Raul Neto, UTA"), ("Georges Niang, UTA", "Georges Niang, UTA"), ("Joakim Noah, MEM", "Joakim Noah, MEM"), ("Nerlens Noel, OKC", "Nerlens Noel, OKC"),
        ("Dirk Nowitzki, DAL", "Dirk Nowitzki, DAL"), ("Frank Ntilikina, NYK", "Frank Ntilikina, NYK"), ("James Nunnally, TOT", "James Nunnally, TOT"), ("James Nunnally, MIN", "James Nunnally, MIN"), ("James Nunnally, HOU", "James Nunnally, HOU"),
        ("Jusuf Nurkic, POR", "Jusuf Nurkic, POR"), ("David Nwaba, CLE", "David Nwaba, CLE"), ("Royce O'Neale, UTA", "Royce O'Neale, UTA"), ("Kyle O'Quinn, IND", "Kyle O'Quinn, IND"), ("Semi Ojeleye, BOS", "Semi Ojeleye, BOS"), ("Jahlil Okafor, NOP", "Jahlil Okafor, NOP"),
        ("Elie Okobo, PHO", "Elie Okobo, PHO"), ("Josh Okogie, MIN", "Josh Okogie, MIN"), ("Victor Oladipo, IND", "Victor Oladipo, IND"), ("Kelly Olynyk, MIA", "Kelly Olynyk, MIA"), ("Cedi Osman, CLE", "Cedi Osman, CLE"), ("Kelly Oubre, TOT", "Kelly Oubre, TOT"),
        ("Kelly Oubre, WAS", "Kelly Oubre, WAS"), ("Kelly Oubre, PHO", "Kelly Oubre, PHO"), ("Zaza Pachulia, DET", "Zaza Pachulia, DET"), ("Jabari Parker, TOT", "Jabari Parker, TOT"), ("Jabari Parker, CHI", "Jabari Parker, CHI"), ("Jabari Parker, WAS", "Jabari Parker, WAS"),
        ("Tony Parker, CHO", "Tony Parker, CHO"), ("Chandler Parsons, MEM", "Chandler Parsons, MEM"), ("Patrick Patterson, OKC", "Patrick Patterson, OKC"), ("Justin Patton, PHI", "Justin Patton, PHI"),
        ("Chris Paul, HOU", "Chris Paul, HOU"), ("Cameron Payne, TOT", "Cameron Payne, TOT"), ("Cameron Payne, CHI", "Cameron Payne, CHI"), ("Cameron Payne, CLE", "Cameron Payne, CLE"), ("Elfrid Payton, NOP", "Elfrid Payton, NOP"), ("Gary Payton, WAS", "Gary Payton, WAS"),
        ("Theo Pinson, BRK", "Theo Pinson, BRK"), ("Mason Plumlee, DEN", "Mason Plumlee, DEN"), ("Miles Plumlee, ATL", "Miles Plumlee, ATL"), ("Jakob Poeltl, SAS", "Jakob Poeltl, SAS"), ("Quincy Pondexter, SAS", "Quincy Pondexter, SAS"), ("Otto Porter, TOT", "Otto Porter, TOT"),
        ("Otto Porter, WAS", "Otto Porter, WAS"), ("Otto Porter, CHI", "Otto Porter, CHI"), ("Bobby Portis, TOT", "Bobby Portis, TOT"), ("Bobby Portis, CHI", "Bobby Portis, CHI"), ("Bobby Portis, WAS", "Bobby Portis, WAS"), ("Dwight Powell, DAL", "Dwight Powell, DAL"),
        ("Norman Powell, TOR", "Norman Powell, TOR"), ("Alex Poythress, ATL", "Alex Poythress, ATL"), ("Zhou Qi, HOU", "Zhou Qi, HOU"), ("Ivan Rabb, MEM", "Ivan Rabb, MEM"), ("Chasson Randle, WAS", "Chasson Randle, WAS"), ("Julius Randle, NOP", "Julius Randle, NOP"),
        ("J.J. Redick, PHI", "J.J. Redick, PHI"), ("Davon Reed, IND", "Davon Reed, IND"), ("Cameron Reynolds, MIN", "Cameron Reynolds, MIN"), ("Josh Richardson, MIA", "Josh Richardson, MIA"), ("Malachi Richardson, TOR", "Malachi Richardson, TOR"),
        ("Austin Rivers, TOT", "Austin Rivers, TOT"), ("Austin Rivers, WAS", "Austin Rivers, WAS"), ("Austin Rivers, HOU", "Austin Rivers, HOU"), ("Devin Robinson, WAS", "Devin Robinson, WAS"), ("Duncan Robinson, MIA", "Duncan Robinson, MIA"),
        ("Glenn Robinson, DET", "Glenn Robinson, DET"), ("Jerome Robinson, LAC", "Jerome Robinson, LAC"), ("Mitchell Robinson, NYK", "Mitchell Robinson, NYK"), ("Rajon Rondo, LAL", "Rajon Rondo, LAL"), ("Derrick Rose, MIN", "Derrick Rose, MIN"),
        ("Terrence Ross, ORL", "Terrence Ross, ORL"), ("Terry Rozier, BOS", "Terry Rozier, BOS"), ("Ricky Rubio, UTA", "Ricky Rubio, UTA"), ("D'Angelo Russell, BRK", "D'Angelo Russell, BRK"), ("Domantas Sabonis, IND", "Domantas Sabonis, IND"),
        ("Brandon Sampson, CHI", "Brandon Sampson, CHI"), ("JaKarr Sampson, CHI", "JaKarr Sampson, CHI"), ("Dario Saric, TOT", "Dario Saric, TOT"), ("Dario Saric, PHI", "Dario Saric, PHI"), ("Dario Saric, MIN", "Dario Saric, MIN"),
        ("Tomas Satoransky, WAS", "Tomas Satoransky, WAS"), ("Dennis Schroder, OKC", "Dennis Schroder, OKC"), ("Mike Scott, TOT", "Mike Scott, TOT"), ("Mike Scott, LAC", "Mike Scott, LAC"), ("Mike Scott, PHI", "Mike Scott, PHI"),
        ("Thabo Sefolosha, UTA", "Thabo Sefolosha, UTA"), ("Wayne Selden, TOT", "Wayne Selden, TOT"), ("Wayne Selden, MEM", "Wayne Selden, MEM"), ("Wayne Selden, CHI", "Wayne Selden, CHI"), ("Collin Sexton, CLE", "Collin Sexton, CLE"),
        ("Landry Shamet, TOT", "Landry Shamet, TOT"), ("Landry Shamet, PHI", "Landry Shamet, PHI"), ("Landry Shamet, LAC", "Landry Shamet, LAC"), ("Iman Shumpert, TOT", "Iman Shumpert, TOT"), ("Iman Shumpert, SAC", "Iman Shumpert, SAC"),
        ("Iman Shumpert, HOU", "Iman Shumpert, HOU"), ("Pascal Siakam, TOR", "Pascal Siakam, TOR"), ("Jordan Sibert, ATL", "Jordan Sibert, ATL"), ("Ben Simmons, PHI", "Ben Simmons, PHI"), ("Jonathon Simmons, TOT", "Jonathon Simmons, TOT"),
        ("Jonathon Simmons, ORL", "Jonathon Simmons, ORL"), ("Jonathon Simmons, PHI", "Jonathon Simmons, PHI"), ("Kobi Simmons, CLE", "Kobi Simmons, CLE"), ("Anfernee Simons, POR", "Anfernee Simons, POR"), ("Marcus Smart, BOS", "Marcus Smart, BOS"),
        ("Dennis Smith, TOT", "Dennis Smith, TOT"), ("Dennis Smith, DAL", "Dennis Smith, DAL"), ("Dennis Smith, NYK", "Dennis Smith, NYK"), ("Ish Smith, DET", "Ish Smith, DET"), ("J.R. Smith, CLE", "J.R. Smith, CLE"), ("Jason Smith, TOT", "Jason Smith, TOT"),
        ("Jason Smith, WAS", "Jason Smith, WAS"), ("Jason Smith, MIL", "Jason Smith, MIL"), ("Jason Smith, NOP", "Jason Smith, NOP"), ("Zhaire Smith, PHI", "Zhaire Smith, PHI"), ("Tony Snell, MIL", "Tony Snell, MIL"), ("Ray Spalding, TOT", "Ray Spalding, TOT"),
        ("Ray Spalding, DAL", "Ray Spalding, DAL"), ("Ray Spalding, PHO", "Ray Spalding, PHO"), ("Omari Spellman, ATL", "Omari Spellman, ATL"), ("Nik Stauskas, TOT", "Nik Stauskas, TOT"), ("Nik Stauskas, POR", "Nik Stauskas, POR"), ("Nik Stauskas, CLE", "Nik Stauskas, CLE"),
        ("D.J. Stephens, MEM", "D.J. Stephens, MEM"), ("Lance Stephenson, LAL", "Lance Stephenson, LAL"), ("Edmond Sumner, IND", "Edmond Sumner, IND"), ("Caleb Swanigan, TOT", "Caleb Swanigan, TOT"), ("Caleb Swanigan, POR", "Caleb Swanigan, POR"),
        ("Caleb Swanigan, SAC", "Caleb Swanigan, SAC"), ("Jayson Tatum, BOS", "Jayson Tatum, BOS"), ("Jeff Teague, MIN", "Jeff Teague, MIN"), ("Garrett Temple, TOT", "Garrett Temple, TOT"), ("Garrett Temple, MEM", "Garrett Temple, MEM"),
        ("Garrett Temple, LAC", "Garrett Temple, LAC"), ("Milos Teodosic, LAC", "Milos Teodosic, LAC"), ("Jared Terrell, MIN", "Jared Terrell, MIN"), ("Emanuel Terry, TOT", "Emanuel Terry, TOT"), ("Emanuel Terry, PHO", "Emanuel Terry, PHO"),
        ("Emanuel Terry, MIA", "Emanuel Terry, MIA"), ("Daniel Theis, BOS", "Daniel Theis, BOS"), ("Isaiah Thomas, DEN", "Isaiah Thomas, DEN"), ("Khyri Thomas, DET", "Khyri Thomas, DET"), ("Lance Thomas, NYK", "Lance Thomas, NYK"),
        ("Klay Thompson, GSW", "Klay Thompson, GSW"), ("Tristan Thompson, CLE", "Tristan Thompson, CLE"), ("Sindarius Thornwell, LAC", "Sindarius Thornwell, LAC"), ("Anthony Tolliver, MIN", "Anthony Tolliver, MIN"), ("Karl-Anthony Towns, MIN", "Karl-Anthony Towns, MIN"),
        ("Gary Trent, POR", "Gary Trent, POR"), ("Allonzo Trier, NYK", "Allonzo Trier, NYK"), ("P.J. Tucker, HOU", "P.J. Tucker, HOU"), ("Evan Turner, POR", "Evan Turner, POR"), ("Myles Turner, IND", "Myles Turner, IND"), ("Ekpe Udoh, UTA", "Ekpe Udoh, UTA"),
        ("Tyler Ulis, CHI", "Tyler Ulis, CHI"), ("Jonas Valanciunas, TOT", "Jonas Valanciunas, TOT"), ("Jonas Valanciunas, TOR", "Jonas Valanciunas, TOR"), ("Jonas Valanciunas, MEM", "Jonas Valanciunas, MEM"),
        ("Jarred Vanderbilt, DEN", "Jarred Vanderbilt, DEN"), ("Fred VanVleet, TOR", "Fred VanVleet, TOR"), ("Noah Vonleh, NYK", "Noah Vonleh, NYK"), ("Nikola Vucevic, ORL", "Nikola Vucevic, ORL"), ("Dwyane Wade, MIA", "Dwyane Wade, MIA"),
        ("Moritz Wagner, LAL", "Moritz Wagner, LAL"), ("Dion Waiters, MIA", "Dion Waiters, MIA"), ("Kemba Walker, CHO", "Kemba Walker, CHO"), ("Lonnie Walker, SAS", "Lonnie Walker, SAS"), ("John Wall, WAS", "John Wall, WAS"),
        ("Tyrone Wallace, LAC", "Tyrone Wallace, LAC"), ("Taurean Waller-Prince, ATL", "Taurean Waller-Prince, ATL"), ("Brad Wanamaker, BOS", "Brad Wanamaker, BOS"), ("T.J. Warren, PHO", "T.J. Warren, PHO"), ("Julian Washburn, MEM", "Julian Washburn, MEM"),
        ("Yuta Watanabe, MEM", "Yuta Watanabe, MEM"), ("Thomas Welsh, DEN", "Thomas Welsh, DEN"), ("Russell Westbrook, OKC", "Russell Westbrook, OKC"), ("Derrick White, SAS", "Derrick White, SAS"), ("Okaro White, WAS", "Okaro White, WAS"),
        ("Hassan Whiteside, MIA", "Hassan Whiteside, MIA"), ("Andrew Wiggins, MIN", "Andrew Wiggins, MIN"), ("Alan Williams, BRK", "Alan Williams, BRK"), ("C.J. Williams, MIN", "C.J. Williams, MIN"), ("Johnathan Williams, LAL", "Johnathan Williams, LAL"),
        ("Kenrich Williams, NOP", "Kenrich Williams, NOP"), ("Lou Williams, LAC", "Lou Williams, LAC"), ("Marvin Williams, CHO", "Marvin Williams, CHO"), ("Robert Williams, BOS", "Robert Williams, BOS"), ("Troy Williams, SAC", "Troy Williams, SAC"),
        ("D.J. Wilson, MIL", "D.J. Wilson, MIL"), ("Justise Winslow, MIA", "Justise Winslow, MIA"), ("Christian Wood, TOT", "Christian Wood, TOT"), ("Christian Wood, MIL", "Christian Wood, MIL"), ("Christian Wood, NOP", "Christian Wood, NOP"),
        ("Delon Wright, TOT", "Delon Wright, TOT"), ("Delon Wright, TOR", "Delon Wright, TOR"), ("Delon Wright, MEM", "Delon Wright, MEM"), ("Guerschon Yabusele, BOS", "Guerschon Yabusele, BOS"), ("Nick Young, DEN", "Nick Young, DEN"),
        ("Thaddeus Young, IND", "Thaddeus Young, IND"), ("Trae Young, ATL", "Trae Young, ATL"), ("Cody Zeller, CHO", "Cody Zeller, CHO"), ("Tyler Zeller, TOT", "Tyler Zeller, TOT"), ("Tyler Zeller, ATL", "Tyler Zeller, ATL"), ("Tyler Zeller, MEM", "Tyler Zeller, MEM"),
        ("Ante Zizic, CLE", "Ante Zizic, CLE"), ("Ivica Zubac, TOT", "Ivica Zubac, TOT"), ("Ivica Zubac, LAL", "Ivica Zubac, LAL"), ("Ivica Zubac, LAC", "Ivica Zubac, LAC")
        ]


class NBAStatForm(FlaskForm):
    name = SelectField(
                       'Name',
                       choices=)
    position = SelectField('Position',
                           choices=[
                           ("", ""), 
                           ("PG", "Point Guard"),
                           ("SG", "Shooting Guard"),
                           ("SF", "Small Forward"),
                           ("PF", "Power Forward"),
                           ("C", "Center")])
    team = SelectField(
            'Team', 
            choices=[("", ""), ("ATL", "Atlanta Hawks"),
            ("BOS", "Boston Celtics"), ("BRK", "Brooklyn Nets"),
            ("CHI", "Chicago Bulls"), ("CHO", "Charlotte Hornets"),
            ("CLE", "Cleveland Cavaliers"), ("DAL", "Dallas Mavericks"),
            ("DEN", "Denver Nuggets"), ("DET", "Detroit Pistons"),
            ("GSW", "Golden State Warriors"), ("HOU", "Houston Rockets"),
            ("IND", "Indiana Pacers"), ("LAC", "Los Angeles Clippers"),
            ("LAL", "Los Angeles Lakers"), ("MEM", "Memphis Grizzlies"),
            ("MIA", "Miami Heat"), ("MIL", "Milwaukee Bucks"),
            ("MIN", "Minnesota Timberwolves"), ("NOP", "New Orleands Pelicans"),
            ("NYK", "New York Knicks"), ("OKC", "Oklahoma City Thunder"),
            ("ORL", "Orlando Magic"), ("PHI", "Your Philadelphia Seventy-Sixers"), 
            ("PHO", "Phoenix Suns"), ("POR", "Portland Trail Blazers"),
            ("SAC", "Sacramento Kings"), ("SAS", "San Antonio Spurs"), 
            ("TOR", "Toronto Raptors"), ("UTA", "Utah Jazz"),
            ("WAS", "Washington Wizards")])
    search_criteria = [
            ('points', 'Points'), ('position', 'Position'),
            ('age', 'Age'), ('games', 'Games Played'),
            ('games_started', 'Games Started'),
            ('minutes_played', 'Minutes Played'),
            ('field_goals', 'Field Goals'),
            ('field_goal_attempts', 'Field Goal Attempts'),
            ('field_goal_percentage', 'Field Goal Percentage'),
            ('three_point_shots_made', 'Three Point Shots Made'),
            ('three_point_attempts', 'Three Point Attempts'),
            ('three_point_percentage', 'Three Point Percentage'),
            ('two_point_shots_made', 'Two Point Shots Made'),
            ('two_point_attempts', 'Two Point Attempts'),
            ('two_point_percentage', 'Two Point Percentage'),
            ('free_throws_made', 'Free Throws Made'),
            ('free_throw_attempts', 'Free Throw Attempts'),
            ('free_throw_percentage', 'Free Throw Percentage'),
            ('defensive_rebounds', 'Defensive Rebounds'),
            ('offensive_rebounds', 'Offensive Rebounds'),
            ('total_rebounds', 'Total Rebounds'),
            ('assists', 'Assists'), ('steals', 'Steals'),
            ('blocks', 'Blocks'), ('turnovers', 'Turnovers'),
            ('personal_fouls', 'Personal Fouls')]

    blank_tuple = (0, "")
    age_list = [(num, num) for num in range(18,43)]
    age_list.insert(0, blank_tuple)
    age = SelectField('Age', coerce=int, default=("", ""),
                      choices=age_list)
    age_range = SelectField(
            'At Least, At Most, Equal To',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most"),
            ("=", "Equal To")]
            )

    games_list = [(num, num) for num in range(5, 81, 5)]
    games_list.insert(0, blank_tuple)
    games = SelectField(
            'Games Played', coerce=int, default=("",""),
            choices=games_list)
    games_range = SelectField(
            'At Least, At Most, Equal To',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most"),
            ("=", "Equal To")])

    games_started = SelectField(
            'Games Started', coerce=int, default=("",""),
            choices=games_list)
    games_started_range = SelectField(
            'At Least, At Most, Equal To',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most"),
            ("=", "Equal To")])

    minutes_list = [(num, num) for num in range(200, 3201, 200)]
    minutes_list.insert(0, blank_tuple)
    minutes_played = SelectField(
            'Minutes Played', coerce=int, default=("",""),
            choices=minutes_list)
    minutes_range = SelectField(
            'At Least, At Most, Equal To',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most"),
            ("=", "Equal To")])

    points_list = [(num, num) for num in range(200, 3001, 200)]
    points_list.insert(0, blank_tuple)
    points = SelectField(
            'Total Points', coerce=int, default=("",""),
            choices=points_list)
    points_range = SelectField(
            'At Least, At Most, Equal To',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most"),
            ("=", "Equal To")])

    field_goal_list = [(num, num) for num in range(100, 901, 100)]
    field_goal_list.insert(0, blank_tuple)
    field_goals = SelectField(
            'Total Field Goals', coerce=int, default=("",""),
            choices=field_goal_list)
    field_goal_range = SelectField(
            'At Least, At Most, Equal To',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most"),
            ("=", "Equal To")])

    field_goal_attempts_list = [
            (num, num) for num in range(200, 2001, 200)]
    field_goal_attempts_list.insert(0, blank_tuple)
    field_goal_attempts = SelectField(
            'Total Field Goal Attempts', coerce=int, default=("",""),
            choices=field_goal_attempts_list)
    field_goal_attempts_range = SelectField(
            'At Least, At Most, Equal To',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most"),
            ("=", "Equal To")])

    field_goal_percentage_list = [
            (num, str(num) + "%") for num in range(5, 105, 5)]
    field_goal_percentage_list.insert(0, blank_tuple)
    field_goal_percentage = SelectField(
            'Field Goal Percentage', coerce=int, default=("",""),
            choices=field_goal_percentage_list)
    field_goal_percentage_range = SelectField(
            'At Least, At Most, Equal To',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    three_point_shots_made_list = [
            (num, num) for num in range(25, 400, 25)]
    three_point_shots_made_list.insert(0, blank_tuple)
    three_point_shots_made = SelectField(
            'Total Three Point Shots Made',
            coerce=int, default=("",""),
            choices=three_point_shots_made_list)
    three_point_shots_made_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    three_point_attempts_list = [
            (num, num) for num in range(50, 1050, 50)]
    three_point_attempts_list.insert(0, blank_tuple)
    three_point_attempts = SelectField(
            'Total Three Point Attempts', coerce=int, default=("",""),
            choices=three_point_attempts_list)
    three_point_attempts_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    three_point_percentage_list = [
            (num, str(num) + "%") for num in range(5, 105, 5)]
    three_point_percentage_list.insert(0, blank_tuple)
    three_point_percentage = SelectField(
            'Three Point Percentage', coerce=int, default=("",""),
            choices=three_point_percentage_list)
    three_point_percentage_range = SelectField(
            'At Least, At Most, Equal To',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    two_point_shots_made_list = [
            (num, num) for num in range(50, 700, 50)]
    two_point_shots_made_list.insert(0, blank_tuple)
    two_point_shots_made = SelectField(
            'Total Two Point Shots Made', coerce=int, default=("",""),
            choices=two_point_shots_made_list)
    two_point_shots_made_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    two_point_attempts_list = [
            (num, num) for num in range(100, 1300, 100)]
    two_point_attempts_list.insert(0, blank_tuple)
    two_point_attempts = SelectField(
            'Total Two Point Attempts', coerce=int, default=("",""),
            choices=two_point_attempts_list)
    two_point_attempts_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    two_point_percentage_list = [
            (num, str(num) + "%") for num in range(5, 105, 5)]
    two_point_percentage_list.insert(0, blank_tuple)
    two_point_percentage = SelectField(
            'Two Point Percentage', coerce=int, default=("",""),
            choices=two_point_percentage_list)
    two_point_percentage_range = SelectField(
            'At Least, At Most, Equal To',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    free_throws_made_list = [(num, num) for num in range(50, 800, 50)]
    free_throws_made_list.insert(0, blank_tuple)
    free_throws_made = SelectField(
            'Total Free Throws Made', coerce=int, default=("",""),
            choices=free_throws_made_list)
    free_throws_made_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    free_throw_attempts_list = [
            (num, num) for num in range(100, 900, 100)]
    free_throw_attempts_list.insert(0, blank_tuple)
    free_throw_attempts = SelectField(
            'Total Free Throw Attempts', coerce=int, default=("",""),
            choices=free_throw_attempts_list)
    free_throw_attempts_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    free_throw_percentage_list = [
            (num, str(num) + "%") for num in range(5, 105, 5)]
    free_throw_percentage_list.insert(0, blank_tuple)
    free_throw_percentage = SelectField(
            'Free Throw Percentage', coerce=int, default=("",""),
            choices=free_throw_percentage_list)
    free_throw_percentage_range = SelectField(
            'At Least, At Most, Equal To',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    offensive_rebounds_list = [
            (num, num) for num in range(25, 425, 25)]
    offensive_rebounds_list.insert(0, blank_tuple)
    offensive_rebounds = SelectField(
            'Total Offensive Rebounds', coerce=int, default=("",""),
            choices=offensive_rebounds_list)
    offensive_rebounds_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    defensive_rebounds_list = [
            (num, num) for num in range(50, 850, 50)]
    defensive_rebounds_list.insert(0, blank_tuple)
    defensive_rebounds = SelectField(
            'Total Defensive Rebounds', coerce=int, default=("",""),
            choices=defensive_rebounds_list)
    defensive_rebounds_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    total_rebounds_list = [
            (num, num) for num in range(100, 1300, 100)]
    total_rebounds_list.insert(0, blank_tuple)
    total_rebounds = SelectField(
            'Total Rebounds', coerce=int, default=("",""),
            choices=total_rebounds_list)
    total_rebounds_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    assists_list = [(num, num) for num in range(50, 800, 50)]
    assists_list.insert(0, blank_tuple)
    assists = SelectField(
            'Total Assists', coerce=int, default=("",""),
            choices=assists_list)
    assists_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    steals_list = [(num, num) for num in range(20, 180, 20)]
    steals_list.insert(0, blank_tuple)
    steals = SelectField(
            'Total Steals', coerce=int, default=("",""),
            choices=steals_list)
    steals_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    blocks_list = [(num, num) for num in range(20, 200, 20)]
    blocks_list.insert(0, blank_tuple)
    blocks = SelectField(
            'Total Blocks', coerce=int, default=("",""),
            choices=blocks_list)
    blocks_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    turnovers_list = [(num, num) for num in range(50, 400, 50)]
    turnovers_list.insert(0, blank_tuple)
    turnovers = SelectField(
            'Total Turnovers', coerce=int, default=("",""),
            choices=turnovers_list)
    turnovers_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    personal_fouls_list = [(num, num) for num in range(50, 300, 50)]
    personal_fouls_list.insert(0, blank_tuple)
    personal_fouls = SelectField(
            'Total Personal Fouls', coerce=int, default=("",""),
            choices=personal_fouls_list)
    personal_fouls_range = SelectField(
            'At Least, At Most',
            choices=[("", ""), (">=", "At Least"), ("<=", "At Most")])

    sort_by_list = search_criteria
    sort_by_list.insert(0, ("", ""))
    sort_by = SelectField(
            'Sort Results By', default=("",""),
            choices=sort_by_list)

    submit_search = SubmitField('Search Database')