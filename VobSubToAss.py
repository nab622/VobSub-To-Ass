#!/usr/bin/env python3

#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007

# Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

#                            Preamble

#  The GNU General Public License is a free, copyleft license for
# software and other kinds of works.

#  The licenses for most software and other practical works are designed
# to take away your freedom to share and change the works.  By contrast,
# the GNU General Public License is intended to guarantee your freedom to
# share and change all versions of a program--to make sure it remains free
# software for all its users.  We, the Free Software Foundation, use the
# GNU General Public License for most of our software; it applies also to
# any other work released this way by its authors.  You can apply it to
# your programs, too.

#  When we speak of free software, we are referring to freedom, not
# price.  Our General Public Licenses are designed to make sure that you
# have the freedom to distribute copies of free software (and charge for
# them if you wish), that you receive source code or can get it if you
# want it, that you can change the software or use pieces of it in new
# free programs, and that you know you can do these things.

#  To protect your rights, we need to prevent others from denying you
# these rights or asking you to surrender the rights.  Therefore, you have
# certain responsibilities if you distribute copies of the software, or if
# you modify it: responsibilities to respect the freedom of others.

#  For example, if you distribute copies of such a program, whether
# gratis or for a fee, you must pass on to the recipients the same
# freedoms that you received.  You must make sure that they, too, receive
# or can get the source code.  And you must show them these terms so they
# know their rights.

#  Developers that use the GNU GPL protect your rights with two steps:
# (1) assert copyright on the software, and (2) offer you this License
# giving you legal permission to copy, distribute and/or modify it.

#  For the developers' and authors' protection, the GPL clearly explains
# that there is no warranty for this free software.  For both users' and
# authors' sake, the GPL requires that modified versions be marked as
# changed, so that their problems will not be attributed erroneously to
# authors of previous versions.

#  Some devices are designed to deny users access to install or run
# modified versions of the software inside them, although the manufacturer
# can do so.  This is fundamentally incompatible with the aim of
# protecting users' freedom to change the software.  The systematic
# pattern of such abuse occurs in the area of products for individuals to
# use, which is precisely where it is most unacceptable.  Therefore, we
# have designed this version of the GPL to prohibit the practice for those
# products.  If such problems arise substantially in other domains, we
# stand ready to extend this provision to those domains in future versions
# of the GPL, as needed to protect the freedom of users.

#  Finally, every program is threatened constantly by software patents.
# States should not allow patents to restrict development and use of
# software on general-purpose computers, but in those that do, we wish to
# avoid the special danger that patents applied to a free program could
# make it effectively proprietary.  To prevent this, the GPL assures that
# patents cannot be used to render the program non-free.

#  The precise terms and conditions for copying, distribution and
# modification follow.

#                       TERMS AND CONDITIONS

#  0. Definitions.

#  "This License" refers to version 3 of the GNU General Public License.

#  "Copyright" also means copyright-like laws that apply to other kinds of
# works, such as semiconductor masks.

#  "The Program" refers to any copyrightable work licensed under this
# License.  Each licensee is addressed as "you".  "Licensees" and
# "recipients" may be individuals or organizations.

#  To "modify" a work means to copy from or adapt all or part of the work
# in a fashion requiring copyright permission, other than the making of an
# exact copy.  The resulting work is called a "modified version" of the
# earlier work or a work "based on" the earlier work.

#  A "covered work" means either the unmodified Program or a work based
# on the Program.

#  To "propagate" a work means to do anything with it that, without
# permission, would make you directly or secondarily liable for
# infringement under applicable copyright law, except executing it on a
# computer or modifying a private copy.  Propagation includes copying,
# distribution (with or without modification), making available to the
# public, and in some countries other activities as well.

#  To "convey" a work means any kind of propagation that enables other
# parties to make or receive copies.  Mere interaction with a user through
# a computer network, with no transfer of a copy, is not conveying.

#  An interactive user interface displays "Appropriate Legal Notices"
# to the extent that it includes a convenient and prominently visible
# feature that (1) displays an appropriate copyright notice, and (2)
# tells the user that there is no warranty for the work (except to the
# extent that warranties are provided), that licensees may convey the
# work under this License, and how to view a copy of this License.  If
# the interface presents a list of user commands or options, such as a
# menu, a prominent item in the list meets this criterion.

#  1. Source Code.

#  The "source code" for a work means the preferred form of the work
# for making modifications to it.  "Object code" means any non-source
# form of a work.

#  A "Standard Interface" means an interface that either is an official
# standard defined by a recognized standards body, or, in the case of
# interfaces specified for a particular programming language, one that
# is widely used among developers working in that language.

#  The "System Libraries" of an executable work include anything, other
# than the work as a whole, that (a) is included in the normal form of
# packaging a Major Component, but which is not part of that Major
# Component, and (b) serves only to enable use of the work with that
# Major Component, or to implement a Standard Interface for which an
# implementation is available to the public in source code form.  A
# "Major Component", in this context, means a major essential component
# (kernel, window system, and so on) of the specific operating system
# (if any) on which the executable work runs, or a compiler used to
# produce the work, or an object code interpreter used to run it.

#  The "Corresponding Source" for a work in object code form means all
# the source code needed to generate, install, and (for an executable
# work) run the object code and to modify the work, including scripts to
# control those activities.  However, it does not include the work's
# System Libraries, or general-purpose tools or generally available free
# programs which are used unmodified in performing those activities but
# which are not part of the work.  For example, Corresponding Source
# includes interface definition files associated with source files for
# the work, and the source code for shared libraries and dynamically
# linked subprograms that the work is specifically designed to require,
# such as by intimate data communication or control flow between those
# subprograms and other parts of the work.

#  The Corresponding Source need not include anything that users
# can regenerate automatically from other parts of the Corresponding
# Source.

#  The Corresponding Source for a work in source code form is that
# same work.

#  2. Basic Permissions.

#  All rights granted under this License are granted for the term of
# copyright on the Program, and are irrevocable provided the stated
# conditions are met.  This License explicitly affirms your unlimited
# permission to run the unmodified Program.  The output from running a
# covered work is covered by this License only if the output, given its
# content, constitutes a covered work.  This License acknowledges your
# rights of fair use or other equivalent, as provided by copyright law.

#  You may make, run and propagate covered works that you do not
# convey, without conditions so long as your license otherwise remains
# in force.  You may convey covered works to others for the sole purpose
# of having them make modifications exclusively for you, or provide you
# with facilities for running those works, provided that you comply with
# the terms of this License in conveying all material for which you do
# not control copyright.  Those thus making or running the covered works
# for you must do so exclusively on your behalf, under your direction
# and control, on terms that prohibit them from making any copies of
# your copyrighted material outside their relationship with you.

#  Conveying under any other circumstances is permitted solely under
# the conditions stated below.  Sublicensing is not allowed; section 10
# makes it unnecessary.

#  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

#  No covered work shall be deemed part of an effective technological
# measure under any applicable law fulfilling obligations under article
# 11 of the WIPO copyright treaty adopted on 20 December 1996, or
# similar laws prohibiting or restricting circumvention of such
# measures.

#  When you convey a covered work, you waive any legal power to forbid
# circumvention of technological measures to the extent such circumvention
# is effected by exercising rights under this License with respect to
# the covered work, and you disclaim any intention to limit operation or
# modification of the work as a means of enforcing, against the work's
# users, your or third parties' legal rights to forbid circumvention of
# technological measures.

#  4. Conveying Verbatim Copies.

#  You may convey verbatim copies of the Program's source code as you
# receive it, in any medium, provided that you conspicuously and
# appropriately publish on each copy an appropriate copyright notice;
# keep intact all notices stating that this License and any
# non-permissive terms added in accord with section 7 apply to the code;
# keep intact all notices of the absence of any warranty; and give all
# recipients a copy of this License along with the Program.

#  You may charge any price or no price for each copy that you convey,
# and you may offer support or warranty protection for a fee.

#  5. Conveying Modified Source Versions.

#  You may convey a work based on the Program, or the modifications to
# produce it from the Program, in the form of source code under the
# terms of section 4, provided that you also meet all of these conditions:

#    a) The work must carry prominent notices stating that you modified
#    it, and giving a relevant date.

#    b) The work must carry prominent notices stating that it is
#    released under this License and any conditions added under section
#    7.  This requirement modifies the requirement in section 4 to
#    "keep intact all notices".

#    c) You must license the entire work, as a whole, under this
#    License to anyone who comes into possession of a copy.  This
#    License will therefore apply, along with any applicable section 7
#    additional terms, to the whole of the work, and all its parts,
#    regardless of how they are packaged.  This License gives no
#    permission to license the work in any other way, but it does not
#    invalidate such permission if you have separately received it.

#    d) If the work has interactive user interfaces, each must display
#    Appropriate Legal Notices; however, if the Program has interactive
#    interfaces that do not display Appropriate Legal Notices, your
#    work need not make them do so.

#  A compilation of a covered work with other separate and independent
# works, which are not by their nature extensions of the covered work,
# and which are not combined with it such as to form a larger program,
# in or on a volume of a storage or distribution medium, is called an
# "aggregate" if the compilation and its resulting copyright are not
# used to limit the access or legal rights of the compilation's users
# beyond what the individual works permit.  Inclusion of a covered work
# in an aggregate does not cause this License to apply to the other
# parts of the aggregate.

#  6. Conveying Non-Source Forms.

#  You may convey a covered work in object code form under the terms
# of sections 4 and 5, provided that you also convey the
# machine-readable Corresponding Source under the terms of this License,
# in one of these ways:

#    a) Convey the object code in, or embodied in, a physical product
#    (including a physical distribution medium), accompanied by the
#    Corresponding Source fixed on a durable physical medium
#    customarily used for software interchange.

#    b) Convey the object code in, or embodied in, a physical product
#    (including a physical distribution medium), accompanied by a
#    written offer, valid for at least three years and valid for as
#    long as you offer spare parts or customer support for that product
#    model, to give anyone who possesses the object code either (1) a
#    copy of the Corresponding Source for all the software in the
#    product that is covered by this License, on a durable physical
#    medium customarily used for software interchange, for a price no
#    more than your reasonable cost of physically performing this
#    conveying of source, or (2) access to copy the
#    Corresponding Source from a network server at no charge.

#    c) Convey individual copies of the object code with a copy of the
#    written offer to provide the Corresponding Source.  This
#    alternative is allowed only occasionally and noncommercially, and
#    only if you received the object code with such an offer, in accord
#    with subsection 6b.

#    d) Convey the object code by offering access from a designated
#    place (gratis or for a charge), and offer equivalent access to the
#    Corresponding Source in the same way through the same place at no
#    further charge.  You need not require recipients to copy the
#    Corresponding Source along with the object code.  If the place to
#    copy the object code is a network server, the Corresponding Source
#    may be on a different server (operated by you or a third party)
#    that supports equivalent copying facilities, provided you maintain
#    clear directions next to the object code saying where to find the
#    Corresponding Source.  Regardless of what server hosts the
#    Corresponding Source, you remain obligated to ensure that it is
#    available for as long as needed to satisfy these requirements.

#    e) Convey the object code using peer-to-peer transmission, provided
#    you inform other peers where the object code and Corresponding
#    Source of the work are being offered to the general public at no
#    charge under subsection 6d.

#  A separable portion of the object code, whose source code is excluded
# from the Corresponding Source as a System Library, need not be
# included in conveying the object code work.

#  A "User Product" is either (1) a "consumer product", which means any
# tangible personal property which is normally used for personal, family,
# or household purposes, or (2) anything designed or sold for incorporation
# into a dwelling.  In determining whether a product is a consumer product,
# doubtful cases shall be resolved in favor of coverage.  For a particular
# product received by a particular user, "normally used" refers to a
# typical or common use of that class of product, regardless of the status
# of the particular user or of the way in which the particular user
# actually uses, or expects or is expected to use, the product.  A product
# is a consumer product regardless of whether the product has substantial
# commercial, industrial or non-consumer uses, unless such uses represent
# the only significant mode of use of the product.

#  "Installation Information" for a User Product means any methods,
# procedures, authorization keys, or other information required to install
# and execute modified versions of a covered work in that User Product from
# a modified version of its Corresponding Source.  The information must
# suffice to ensure that the continued functioning of the modified object
# code is in no case prevented or interfered with solely because
# modification has been made.

#  If you convey an object code work under this section in, or with, or
# specifically for use in, a User Product, and the conveying occurs as
# part of a transaction in which the right of possession and use of the
# User Product is transferred to the recipient in perpetuity or for a
# fixed term (regardless of how the transaction is characterized), the
# Corresponding Source conveyed under this section must be accompanied
# by the Installation Information.  But this requirement does not apply
# if neither you nor any third party retains the ability to install
# modified object code on the User Product (for example, the work has
# been installed in ROM).

#  The requirement to provide Installation Information does not include a
# requirement to continue to provide support service, warranty, or updates
# for a work that has been modified or installed by the recipient, or for
# the User Product in which it has been modified or installed.  Access to a
# network may be denied when the modification itself materially and
# adversely affects the operation of the network or violates the rules and
# protocols for communication across the network.

#  Corresponding Source conveyed, and Installation Information provided,
# in accord with this section must be in a format that is publicly
# documented (and with an implementation available to the public in
# source code form), and must require no special password or key for
# unpacking, reading or copying.

#  7. Additional Terms.

#  "Additional permissions" are terms that supplement the terms of this
# License by making exceptions from one or more of its conditions.
# Additional permissions that are applicable to the entire Program shall
# be treated as though they were included in this License, to the extent
# that they are valid under applicable law.  If additional permissions
# apply only to part of the Program, that part may be used separately
# under those permissions, but the entire Program remains governed by
# this License without regard to the additional permissions.

#  When you convey a copy of a covered work, you may at your option
# remove any additional permissions from that copy, or from any part of
# it.  (Additional permissions may be written to require their own
# removal in certain cases when you modify the work.)  You may place
# additional permissions on material, added by you to a covered work,
# for which you have or can give appropriate copyright permission.

#  Notwithstanding any other provision of this License, for material you
# add to a covered work, you may (if authorized by the copyright holders of
# that material) supplement the terms of this License with terms:

#    a) Disclaiming warranty or limiting liability differently from the
#    terms of sections 15 and 16 of this License; or

#    b) Requiring preservation of specified reasonable legal notices or
#    author attributions in that material or in the Appropriate Legal
#    Notices displayed by works containing it; or

#    c) Prohibiting misrepresentation of the origin of that material, or
#    requiring that modified versions of such material be marked in
#    reasonable ways as different from the original version; or

#    d) Limiting the use for publicity purposes of names of licensors or
#    authors of the material; or

#    e) Declining to grant rights under trademark law for use of some
#    trade names, trademarks, or service marks; or

#    f) Requiring indemnification of licensors and authors of that
#    material by anyone who conveys the material (or modified versions of
#    it) with contractual assumptions of liability to the recipient, for
#    any liability that these contractual assumptions directly impose on
#    those licensors and authors.

#  All other non-permissive additional terms are considered "further
# restrictions" within the meaning of section 10.  If the Program as you
# received it, or any part of it, contains a notice stating that it is
# governed by this License along with a term that is a further
# restriction, you may remove that term.  If a license document contains
# a further restriction but permits relicensing or conveying under this
# License, you may add to a covered work material governed by the terms
# of that license document, provided that the further restriction does
# not survive such relicensing or conveying.

#  If you add terms to a covered work in accord with this section, you
# must place, in the relevant source files, a statement of the
# additional terms that apply to those files, or a notice indicating
# where to find the applicable terms.

#  Additional terms, permissive or non-permissive, may be stated in the
# form of a separately written license, or stated as exceptions;
# the above requirements apply either way.

#  8. Termination.

#  You may not propagate or modify a covered work except as expressly
# provided under this License.  Any attempt otherwise to propagate or
# modify it is void, and will automatically terminate your rights under
# this License (including any patent licenses granted under the third
# paragraph of section 11).

#  However, if you cease all violation of this License, then your
# license from a particular copyright holder is reinstated (a)
# provisionally, unless and until the copyright holder explicitly and
# finally terminates your license, and (b) permanently, if the copyright
# holder fails to notify you of the violation by some reasonable means
# prior to 60 days after the cessation.

#  Moreover, your license from a particular copyright holder is
# reinstated permanently if the copyright holder notifies you of the
# violation by some reasonable means, this is the first time you have
# received notice of violation of this License (for any work) from that
# copyright holder, and you cure the violation prior to 30 days after
# your receipt of the notice.

#  Termination of your rights under this section does not terminate the
# licenses of parties who have received copies or rights from you under
# this License.  If your rights have been terminated and not permanently
# reinstated, you do not qualify to receive new licenses for the same
# material under section 10.

#  9. Acceptance Not Required for Having Copies.

#  You are not required to accept this License in order to receive or
# run a copy of the Program.  Ancillary propagation of a covered work
# occurring solely as a consequence of using peer-to-peer transmission
# to receive a copy likewise does not require acceptance.  However,
# nothing other than this License grants you permission to propagate or
# modify any covered work.  These actions infringe copyright if you do
# not accept this License.  Therefore, by modifying or propagating a
# covered work, you indicate your acceptance of this License to do so.

#  10. Automatic Licensing of Downstream Recipients.

#  Each time you convey a covered work, the recipient automatically
# receives a license from the original licensors, to run, modify and
# propagate that work, subject to this License.  You are not responsible
# for enforcing compliance by third parties with this License.

#  An "entity transaction" is a transaction transferring control of an
# organization, or substantially all assets of one, or subdividing an
# organization, or merging organizations.  If propagation of a covered
# work results from an entity transaction, each party to that
# transaction who receives a copy of the work also receives whatever
# licenses to the work the party's predecessor in interest had or could
# give under the previous paragraph, plus a right to possession of the
# Corresponding Source of the work from the predecessor in interest, if
# the predecessor has it or can get it with reasonable efforts.

#  You may not impose any further restrictions on the exercise of the
# rights granted or affirmed under this License.  For example, you may
# not impose a license fee, royalty, or other charge for exercise of
# rights granted under this License, and you may not initiate litigation
# (including a cross-claim or counterclaim in a lawsuit) alleging that
# any patent claim is infringed by making, using, selling, offering for
# sale, or importing the Program or any portion of it.

#  11. Patents.

#  A "contributor" is a copyright holder who authorizes use under this
# License of the Program or a work on which the Program is based.  The
# work thus licensed is called the contributor's "contributor version".

#  A contributor's "essential patent claims" are all patent claims
# owned or controlled by the contributor, whether already acquired or
# hereafter acquired, that would be infringed by some manner, permitted
# by this License, of making, using, or selling its contributor version,
# but do not include claims that would be infringed only as a
# consequence of further modification of the contributor version.  For
# purposes of this definition, "control" includes the right to grant
# patent sublicenses in a manner consistent with the requirements of
# this License.

#  Each contributor grants you a non-exclusive, worldwide, royalty-free
# patent license under the contributor's essential patent claims, to
# make, use, sell, offer for sale, import and otherwise run, modify and
# propagate the contents of its contributor version.

#  In the following three paragraphs, a "patent license" is any express
# agreement or commitment, however denominated, not to enforce a patent
# (such as an express permission to practice a patent or covenant not to
# sue for patent infringement).  To "grant" such a patent license to a
# party means to make such an agreement or commitment not to enforce a
# patent against the party.

#  If you convey a covered work, knowingly relying on a patent license,
# and the Corresponding Source of the work is not available for anyone
# to copy, free of charge and under the terms of this License, through a
# publicly available network server or other readily accessible means,
# then you must either (1) cause the Corresponding Source to be so
# available, or (2) arrange to deprive yourself of the benefit of the
# patent license for this particular work, or (3) arrange, in a manner
# consistent with the requirements of this License, to extend the patent
# license to downstream recipients.  "Knowingly relying" means you have
# actual knowledge that, but for the patent license, your conveying the
# covered work in a country, or your recipient's use of the covered work
# in a country, would infringe one or more identifiable patents in that
# country that you have reason to believe are valid.

#  If, pursuant to or in connection with a single transaction or
# arrangement, you convey, or propagate by procuring conveyance of, a
# covered work, and grant a patent license to some of the parties
# receiving the covered work authorizing them to use, propagate, modify
# or convey a specific copy of the covered work, then the patent license
# you grant is automatically extended to all recipients of the covered
# work and works based on it.

#  A patent license is "discriminatory" if it does not include within
# the scope of its coverage, prohibits the exercise of, or is
# conditioned on the non-exercise of one or more of the rights that are
# specifically granted under this License.  You may not convey a covered
# work if you are a party to an arrangement with a third party that is
# in the business of distributing software, under which you make payment
# to the third party based on the extent of your activity of conveying
# the work, and under which the third party grants, to any of the
# parties who would receive the covered work from you, a discriminatory
# patent license (a) in connection with copies of the covered work
# conveyed by you (or copies made from those copies), or (b) primarily
# for and in connection with specific products or compilations that
# contain the covered work, unless you entered into that arrangement,
# or that patent license was granted, prior to 28 March 2007.

#  Nothing in this License shall be construed as excluding or limiting
# any implied license or other defenses to infringement that may
# otherwise be available to you under applicable patent law.

#  12. No Surrender of Others' Freedom.

#  If conditions are imposed on you (whether by court order, agreement or
# otherwise) that contradict the conditions of this License, they do not
# excuse you from the conditions of this License.  If you cannot convey a
# covered work so as to satisfy simultaneously your obligations under this
# License and any other pertinent obligations, then as a consequence you may
# not convey it at all.  For example, if you agree to terms that obligate you
# to collect a royalty for further conveying from those to whom you convey
# the Program, the only way you could satisfy both those terms and this
# License would be to refrain entirely from conveying the Program.

#  13. Use with the GNU Affero General Public License.

#  Notwithstanding any other provision of this License, you have
# permission to link or combine any covered work with a work licensed
# under version 3 of the GNU Affero General Public License into a single
# combined work, and to convey the resulting work.  The terms of this
# License will continue to apply to the part which is the covered work,
# but the special requirements of the GNU Affero General Public License,
# section 13, concerning interaction through a network will apply to the
# combination as such.

#  14. Revised Versions of this License.

#  The Free Software Foundation may publish revised and/or new versions of
# the GNU General Public License from time to time.  Such new versions will
# be similar in spirit to the present version, but may differ in detail to
# address new problems or concerns.

#  Each version is given a distinguishing version number.  If the
# Program specifies that a certain numbered version of the GNU General
# Public License "or any later version" applies to it, you have the
# option of following the terms and conditions either of that numbered
# version or of any later version published by the Free Software
# Foundation.  If the Program does not specify a version number of the
# GNU General Public License, you may choose any version ever published
# by the Free Software Foundation.

#  If the Program specifies that a proxy can decide which future
# versions of the GNU General Public License can be used, that proxy's
# public statement of acceptance of a version permanently authorizes you
# to choose that version for the Program.

#  Later license versions may give you additional or different
# permissions.  However, no additional obligations are imposed on any
# author or copyright holder as a result of your choosing to follow a
# later version.

#  15. Disclaimer of Warranty.

#  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
# APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
# HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
# OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
# IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
# ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

#  16. Limitation of Liability.

#  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
# WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
# THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
# GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
# USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
# DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
# PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
# EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGES.

#  17. Interpretation of Sections 15 and 16.

#  If the disclaimer of warranty and limitation of liability provided
# above cannot be given local legal effect according to their terms,
# reviewing courts shall apply local law that most closely approximates
# an absolute waiver of all civil liability in connection with the
# Program, unless a warranty or assumption of liability accompanies a
# copy of the Program in return for a fee.

#                     END OF TERMS AND CONDITIONS

#            How to Apply These Terms to Your New Programs

#  If you develop a new program, and you want it to be of the greatest
# possible use to the public, the best way to achieve this is to make it
# free software which everyone can redistribute and change under these terms.

#  To do so, attach the following notices to the program.  It is safest
# to attach them to the start of each source file to most effectively
# state the exclusion of warranty; and each file should have at least
# the "copyright" line and a pointer to where the full notice is found.

#    <one line to give the program's name and a brief idea of what it does.>
#    Copyright (C) <year>  <name of author>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Also add information on how to contact you by electronic and paper mail.

#  If the program does terminal interaction, make it output a short
# notice like this when it starts in an interactive mode:

#    <program>  Copyright (C) <year>  <name of author>
#    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; type `show c' for details.

# The hypothetical commands `show w' and `show c' should show the appropriate
# parts of the General Public License.  Of course, your program's commands
# might be different; for a GUI interface, you would use an "about box".

#  You should also get your employer (if you work as a programmer) or school,
# if any, to sign a "copyright disclaimer" for the program, if necessary.
# For more information on this, and how to apply and follow the GNU GPL, see
# <http://www.gnu.org/licenses/>.

#  The GNU General Public License does not permit incorporating your program
# into proprietary programs.  If your program is a subroutine library, you
# may consider it more useful to permit linking proprietary applications with
# the library.  If this is what you want to do, use the GNU Lesser General
# Public License instead of this License.  But first, please read
# <http://www.gnu.org/philosophy/why-not-lgpl.html>.


import os
import sys
import psutil
import math
import argparse
from typing import List, Union, Tuple
from pathlib import Path
import concurrent.futures
from functools import partial, wraps
from enum import Enum

import copy
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List
import re

import json



pixelFont = {
	'blocks' : [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':' ],
	'spaces' : [ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?' ],
}

# This is the version of the script
scriptVersion = '1.0'

PES_MAX_LENGTH = 2028

minimum_milliseconds_between_lines = 24
subtitle_maximum_display_milliseconds = 15 * 1000


# THESE FUNCTIONS ARE COPIED FROM VCRLIBRARY.PY
# THESE FUNCTIONS ARE COPIED FROM VCRLIBRARY.PY

# Colors to use for the text output
class colors:
	black		=	"\033[0;30m"
	darkRed		=	"\033[0;31m"
	darkGreen	=	"\033[0;32m"
	brown		=	"\033[0;33m"
	darkBlue	=	"\033[0;34m"
	purple		=	"\033[0;35m"
	darkCyan	=	"\033[0;36m"
	lightGray	=	"\033[0;37m"
	darkGray	=	"\033[1;30m"
	red			=	"\033[1;31m"
	green		=	"\033[1;32m"
	yellow		=	"\033[1;33m"
	blue		=	"\033[1;34m"
	pink		=	"\033[1;35m"
	cyan		=	"\033[1;36m"
	white		=	"\033[1;37m"
	none		=	"\033[0m"
	bold		=	'\033[1m'
	underline	=	'\033[4m'

# Used to differentiate different errors and different steps in the debug trace
debugColors = [
	colors.red,
	colors.blue,
	colors.brown,
	colors.cyan,
	colors.yellow,
	colors.purple,
	colors.green
]

sizeColors = [
	colors.purple,
	colors.green,
	colors.blue,
	colors.yellow,
	colors.red,
	colors.darkRed,
	colors.white
]

# Special strings to use for cursor control
class cursorControl:
	up = '\033[1A'
	eraseLine = "\r" + '\033[K'
	eraseRemaining = '\033[K'
	erasePreviousLine = '\033[1A' + "\r" + '\033[K' + '\033[1A'
	eraseNextLine = "\r" + '\033[K' + '\033[1A'
def clamp(value, input2, input3):
	if input2 > input3:
		inputMax = input2
		inputMin = input3
	else:
		inputMax = input3
		inputMin = input2

	if value > inputMax:
		return inputMax
	if value < inputMin:
		return inputMin
	return value

def printDebug(*args):
	global debugColors

	messages = args
	i = 0
	while i < len(messages):
		print(debugColors[i % len(debugColors)])
		print(messages[i])
		print(colors.none)
		i += 1

def printAndLog(inputStuff = '', logFile = ''):
	for item in inputStuff:
		print(item)

def prepCommandToPrint(command):
	output = ''

	temp = copy.deepcopy(command)

	triggerQuotes = [ ' ', '|', '[', ']' ]

	for i in range(len(temp)):
		for trigger in triggerQuotes:
			match = False
			if temp[i].find(trigger) >= 0:
				match = True
				temp[i] = '"' + temp[i].replace('"', '\\' + trigger) + '"'
				break

	output = ' '.join(temp)

	return output

def printCommand(command):
	output = ''
	printDebug(prepCommandToPrint(command))

palettePrintCount = 0
paletteColors = [ colors.white, colors.yellow, colors.blue, colors.green, colors.red ]
def printPalette(palette):
	global palettePrintCount

	temp = []
	for i in range(len(palette)):
		if type(palette[i]) is dict:
			temp.append(normalizedRgbToHex(palette[i]))
		else:
			temp.append(palette[i])
	print(paletteColors[palettePrintCount % len(paletteColors)], temp, colors.none)
	palettePrintCount += 1

def printSubtitleToConsole(imageData):
	# This function is used to debug the image arrays after decoding

	colors = []

	print()
	for y in range(len(imageData)):
		if type(imageData[y]) is int:
			print()
			continue
		row = ''
		for x in range(len(imageData[y])):
			if type(imageData[y][x]) is int:
				row += ' '
				continue
			match = -1
			for c in range(len(colors)):
				if areColorsTheSame(imageData[y][x], colors[c]):
					match = c
					break
			if match == -1:
				match = 0
				colors.append(imageData[y][x])
			row += str(match)
		print(row)
	print()

def displayProgress(percentComplete, pass_number = 1, pos = 0, total = -1):
	totalPasses = 2

	offset = 100 / totalPasses * (pass_number - 1)

	percentComplete = float(round((percentComplete / totalPasses + offset), 1))

	index = ''
	if total > 0:
		numLength = len(str(total)) + 2 # Add space, this helps with parsing colors
		index = colors.yellow + leadingSpaces(pos, numLength) + colors.none + '  /' + colors.red + leadingSpaces(total, numLength)
	sys.stdout.flush()
	print(cursorControl.up + cursorControl.eraseRemaining + colors.blue + 'Pass: ' + colors.yellow + str(pass_number) + colors.none + ' / ' + colors.red + str(totalPasses) + '  ' + colors.white + '  ' + leadingSpaces(percentComplete, 4) + '%    ' + index + colors.none)
	sys.stdout.flush()

def padHexColor(hexColor):
	while 2 - len(hexColor) > 0:
		hexColor = '0' + hexColor
	return hexColor

def leadingSpaces(inputNumber, places):
	output = str(inputNumber)
	if isinstance(inputNumber, str):
		placesToAdd = places - len(str(inputNumber))
	else:
		placesToAdd = places - len(str(math.floor(inputNumber)))

	if placesToAdd > 0:
		return ' ' * placesToAdd + output
	else:
		return output

def readFile(filename):
	with open(filename, 'r') as f:
		contents = f.read()
	return contents

def readJSONFile(filename):
	final = {}
	with open(filename, 'r') as f:
		data = f.read()
		final = json.loads(data)
	return final

def setDuration(inputData):
	return [
		# This value is given in microseconds. The ENTIRE VIDEO must be analyzed
#		'-analyzeduration', str(int(inputData['maxDuration'] * 1000000)),
		'-analyzeduration', str(99999999 * 1000000),	# Duration has a chance of being reported wrong. Force an insane value here, make FFmpeg check *everything*

		# This value is given in bytes
		'-probesize', str(int(inputData['fileSize']))
	]

def idxToRGB(color):
	# Apparently IDX files are calculated wrong and are neither RGB nor YUV. What a shock, another bug.
	return YUVStringToRGBString(vobsub_rgb_to_yuv(int(color, 16)))

def av_clip_uint8(value):
	return max(0, min(255, value))

def vobsub_rgb_to_yuv(rgb):
	# This function was modeled after mplayer's source code. Apparently IDX files are calculated wrong
	# and are neither RGB nor YUV. What a shock, another bug.

	r = (rgb >> 16) & 0xff
	g = (rgb >> 8) & 0xff
	b = rgb & 0xff

	y = (0.299 * r + 0.587 * g + 0.114 * b) * 219 / 255 + 16.5
	u = (-0.16874 * r - 0.33126 * g + 0.5 * b) * 224 / 255 + 128.5
	v = (0.5 * r - 0.41869 * g - 0.08131 * b) * 224 / 255 + 128.5

	return intColorToHexColor(int(y) << 16 | int(u) << 8 | int(v))

def normalizedColorToHexColor(color):
	return intColorToHexColor(int(color * 255))

def intColorToHexColor(color):
	output = intToHex(color)
	if len(output) < 2:
		output = '0' + output
	return output

def intColorToAssColor(colorList):
	outputColors = []

	while len(colorList) < 4:
		colorList.append(255)

	for i in range(3):
		outputColors.append(intColorToHexColor(colorList[i]).upper())

	# Alphas are inverted!
	outputColors.append(intColorToHexColor(255-colorList[3]).upper())

	outputColors.reverse()

	if len(colorList) == 4:
		# AABBGGRR
		return '&H' + ''.join(outputColors)
	else:
		# BBGGRR
		return '&H' + ''.join(outputColors)

def intToHex(intValue):
	return hex(intValue).split('x').pop()

def YUVStringToRGBString(inputString):
	# This function takes a 6-digit hexadecimal value for YUV color and converts it to RGB
	output = ''
	tempColors = YUVToRGB(int(inputString[0:2], 16), int(inputString[2:4], 16), int(inputString[4:6], 16))

	i = 0
	while i < len(tempColors):
		tempColors[i] = hex(tempColors[i])
		tempColors[i] = tempColors[i].split('0x')[1]
		j = 2 - len(tempColors[i])
		while j > 0:
			tempColors[i] = '0' + tempColors[i]
			j -= 1
		i += 1

	return ''.join(tempColors)

def RGBStringToYUVString(inputString):
	# This function takes a 6-digit hexadecimal value for RGB color and converts it to YUV
	output = ''
	tempColors = RGBToYUV(int(inputString[0:2], 16), int(inputString[2:4], 16), int(inputString[4:6], 16))

	i = 0
	while i < len(tempColors):
		tempColors[i] = hex(tempColors[i])
		tempColors[i] = tempColors[i].split('0x')[1]
		j = 2 - len(tempColors[i])
		while j > 0:
			tempColors[i] = '0' + tempColors[i]
			j -= 1
		i += 1

	return ''.join(tempColors)

def YUVToRGB(y, u, v):
	r = y + 1.402 * (v - 128)
	g = y - 0.344136 * (u - 128) - 0.714136 * (v - 128)
	b = y + 1.772 * (u - 128)

	# Clamp values to the range [0, 255] and convert to integers
	r = max(0, min(255, int(r)))
	g = max(0, min(255, int(g)))
	b = max(0, min(255, int(b)))

	return [ r, g, b ]

def timeToSeconds(inputString, delimiter = ':'):
	time = 0

	if type(inputString) is str:
		inputString = inputString.strip()
		if len(inputString) > 0:
			inputString = inputString.split(delimiter)

			# Add seconds
			time += float(inputString.pop().strip())

			if len(inputString) > 0:
				# Add minutes
				time += int(inputString.pop().strip()) * 60

				if len(inputString) > 0:
					# Add hours
					time += int(inputString.pop().strip()) * 3600

					if len(inputString) > 0:
						# Add days
						time += int(inputString.pop().strip()) * 3600 * 24

						if len(inputString) > 0:
							# Add weeks
							time += int(inputString.pop().strip()) * 3600 * 24 * 7

							if len(inputString) > 0:
								# User is crazy. Ignore anything that remains.
								pass
	return time

def leadingZeroes(inputNumber, places):
	output = str(inputNumber)
	placesToAdd = places - len(str(math.floor(inputNumber)))
	if placesToAdd > 0:
		return '0' * placesToAdd + output
	else:
		return output

def secondsToTime(inputTime, decimalPrecision = 2):
	hours = str(math.floor(inputTime / 3600))
	minutes = leadingZeroes(math.floor(inputTime % 3600 / 60), 2)
	seconds = leadingZeroes(math.floor(inputTime % 60), 2)
	milliseconds = str(inputTime % 1) + '0'

	return hours + ':' + minutes + ':' + seconds + '.' + milliseconds[2:4]

def alignTimesToDecimalPoint(time):
	# time must be a STRING formatted as:  hh:mm:ss:ms

	time = time.strip()		# Eliminate trailing spaces, we won't need those here

	minLength = 12	# Number of characters to use for the time
	if ':' in time:
		tempTime = time.split(':')
		tempTime[0] = str(int(tempTime[0])) 	# Make sure any leading zeroes on the first number are gone, it's easier to read this way
		time = ':'.join(tempTime)
	else:
		time = str(float(time)) 	# Make sure any leading zeroes on the first number are gone, it's easier to read this way

	if '.' in time:
		tempTime = time.split('.')
		tempTime[1] = tempTime[1] + (' ' * (3 - len(tempTime[1])))
		time = '.'.join(tempTime)
	else:
		time += '    '	# No decimal point. Add 4 spaces

	time = (' ' * (minLength - len(time))) + time
	return time

# THESE FUNCTIONS ARE COPIED FROM VCRLIBRARY.PY
# THESE FUNCTIONS ARE COPIED FROM VCRLIBRARY.PY


@dataclass
class Rectangle:
	x: int = 0
	y: int = 0
	width: int = 0
	height: int = 0

@dataclass
class IdxParagraph:
	start_time: datetime
	file_position: int

def wrapper(method):
	@wraps(method)
	def wrapped(*args, **kwargs):
		r = method(*args, **kwargs)
		return r
		if isinstance(r, timedelta):
			return r
		else:
			return r
	return wrapped

class TimeDeltaMetaClass(type):
	def __new__(meta, classname, bases, class_dict):
		class_ = super().__new__(meta, classname, bases, class_dict)
		new_class_dict = {}
		for attribute_name in dir(class_):
			if attribute_name in ['__init__', '__new__', '__class__', '__dict__']:
				continue
			# if hasattr(attribute, '__call__'):
			# if type(attribute) == FunctionType:
				# attribute = wrapper(attribute)
			attribute = getattr(class_, attribute_name)
			setattr(class_, attribute_name,  wrapper(attribute))
			# new_class_dict[attributeName] = attribute
		# return super().__new__(meta, classname, bases, new_class_dict)
		return class_

def generateImageList(width, height, colorCount = 4):
	testOutput = colors.white + str(width) + '   ' +  str(height)

	output = []

	color = []
	while len(color) < colorCount:
		color.append(0)

	while len(output) < height:
		row = []
		while len(row) < width:
			row.append(color)
		output.append(row)

	return output

class SubPicture:
# Subtitle Picture - see http:#www.mpucoder.com/DVD/spu.html for more info
# http://sam.zoy.org/writings/dvd/subtitles/

	class DisplayControlCommand(Enum):
		ForcedStartDisplay = 0
		StartDisplay = 1
		StopDisplay = 2
		SetColor = 3
		SetContrast = 4
		SetDisplayArea = 5
		SetPixelDataAddress = 6
		ChangeColorAndContrast = 7
		End = 0xFF

	def __init__(
		self, data: bytes,
		start_display_control_sequence_table_address: int = None,
		pixel_data_address_offset: int = 0
	):
		"""
		For SP packet with DVD sub pictures
		:param: data: bytes content of the sub pack
		:param: start_display_control_sequence_table_address: Adress of the first control sequence in data
		:param: pixel_data_address_offset: Bitmap pixel data address offset
		"""
		self._data = data
		self.forced = False
		self.delay = timedelta()
		self.duration = 0
		self.sub_picture_data_size = get_endian_word(self._data, 0)
		self._pixel_data_address_offset = pixel_data_address_offset
		if start_display_control_sequence_table_address is None and pixel_data_address_offset is None:
			self._start_display_control_sequence_table_address = start_display_control_sequence_table_address
		else:
			self._start_display_control_sequence_table_address = get_endian_word(self._data, 2)
			self.sub_picture_data_size = len(self._data)
		self.parse_display_control_commands(False, None, None, False, False)

	def get_bitmap(
		self,
		color_lookup_table: list[list],
		background: list,
		pattern: list,
		emphasis1: list,
		emphasis2: list,
		use_custom_colors: bool,
		crop: bool = True
	):
		"""
		Generates the current subtitle image
		:param: color_lookup_table: The Color LookUp Table (CLUT), if null then only the four colors are used (should contain 16 elements if not null)
		:param: background: Background color
		:param: pattern: Color
		:param: emphasis1: Color
		:param: emphasis2: Color
		:param: use_custom_colors: Use custom colors instead of lookup table
		:param: crop: Crop result image

		:return: Subtitle image
		"""
		four_colors = [background, pattern, emphasis1, emphasis2]

		return self.parse_display_control_commands(True, color_lookup_table, copy.deepcopy(four_colors), use_custom_colors, crop)

	def parse_display_control_commands(
		self,
		create_bitmap: bool,
		color_look_up_table: list[list],
		four_colors: list[list],
		use_custom_colors: bool,
		crop: bool
	):
		self.image_display_area = Rectangle()
		bmp = None
		display_control_sequence_table_addresses = []
		image_top_field_data_address = 0
		image_bottom_field_data_address = 1
		bitmap_generated = False
		largest_delay = -999999
		display_control_sequence_table_address = self._start_display_control_sequence_table_address - self._pixel_data_address_offset
		last_display_control_sequence_table_address = 0
		display_control_sequence_table_addresses.append(display_control_sequence_table_address)
		command_index = 0

		delay = 0

		while (display_control_sequence_table_address > last_display_control_sequence_table_address
			and display_control_sequence_table_address + 1 < len(self._data) and command_index < len(self._data)):

			delay_before_execute = get_endian_word(self._data, display_control_sequence_table_address + self._pixel_data_address_offset)
			command_index = display_control_sequence_table_address + 4 + self._pixel_data_address_offset
			if (command_index >= len(self._data)):
				break ## invalid index

			command = self._data[command_index]
			number_of_commands = 0
			while command != SubPicture.DisplayControlCommand.End.value and number_of_commands < 1000 and command_index < len(self._data):
				number_of_commands += 1
				if command == SubPicture.DisplayControlCommand.ForcedStartDisplay.value: # 0
					self.forced = True
					command_index+=1
				elif command == SubPicture.DisplayControlCommand.StartDisplay.value: # 1
					command_index+=1
				elif command == SubPicture.DisplayControlCommand.StopDisplay.value: # 2
					self.delay = timedelta(milliseconds=(delay_before_execute << 10) / 90.0)
					# OLD CODE HERE
					#if create_bitmap and self.delay.total_seconds() / 1000 > largest_delay: # in case of more than one image, just use the one with the largest display time
					#	largest_delay = self.delay.total_seconds() / 1000
					if create_bitmap and self.delay.total_seconds() > largest_delay: # in case of more than one image, just use the one with the largest display time
						largest_delay = self.delay.total_seconds()
						# bmp?.Dispose() # Release the image memory
						bmp = self.generate_bitmap(self.image_display_area, image_top_field_data_address, image_bottom_field_data_address, four_colors, crop)
						bitmap_generated = True
					command_index+=1
				elif command == SubPicture.DisplayControlCommand.SetColor.value: # 3
					if color_look_up_table != None and type(four_colors) is list:
						imageColor = [self._data[command_index + 1], self._data[command_index + 2]]
						if not use_custom_colors:
							four_colors = SubPicture.set_color(four_colors, 3, imageColor[0] >> 4, color_look_up_table)
							four_colors = SubPicture.set_color(four_colors, 2, imageColor[0] & 0b00001111, color_look_up_table)
							four_colors = SubPicture.set_color(four_colors, 1, imageColor[1] >> 4, color_look_up_table)
							four_colors = SubPicture.set_color(four_colors, 0, imageColor[1] & 0b00001111, color_look_up_table)
					command_index += 3
				elif command == SubPicture.DisplayControlCommand.SetContrast.value: # 4
					if color_look_up_table != None and type(four_colors) is list:
						imageContrast = [self._data[command_index + 1], self._data[command_index + 2]]
						if imageContrast[0] + imageContrast[1] > 0:
							# Get an alpha value, normalized from 0 to 255
							alpha_colors = [ 255, 255, 255, 255 ]
							
							alpha_colors[3] = (((imageContrast[0] & 0xF0) >> 4) * 17)
							alpha_colors[2] = ((imageContrast[0] & 0b00001111) * 17)
							alpha_colors[1] = (((imageContrast[1] & 0xF0) >> 4) * 17)
							alpha_colors[0] = ((imageContrast[1] & 0b00001111) * 17)

							for c in range(len(alpha_colors)):
								if len(four_colors[c]) < 4:
									four_colors[c].append(alpha_colors[c])
								else:
									four_colors[c][3] = alpha_colors[c]
					command_index += 3
				elif command == SubPicture.DisplayControlCommand.SetDisplayArea.value: # 5
					if len(self._data) > command_index + 6 and self.image_display_area.width == 0 and self.image_display_area.height == 0:

						# Original code
						# THIS IS HERE JUST IN CASE MY CORRECTION IS WRONG. THIS METHOD IS BROKEN ON RANDOM SUBTITLES
						# ~ starting_x = (self._data[command_index + 1] << 8 | self._data[command_index + 2]) >> 4
						# ~ ending_x = (self._data[command_index + 2] & 0b00001111) << 8 | self._data[command_index + 3] + 1
						# ~ starting_y = (self._data[command_index + 4] << 8 | self._data[command_index + 5]) >> 4
						# ~ ending_y = (self._data[command_index + 5] & 0b00001111) << 8 | self._data[command_index + 6] + 1

						# My code
						# WHY WAS THERE A BITWISE_OR IN THE ORIGINAL CODE, IT MAKES NO SENSE, THESE ARE UNSIGNED INTs THAT NEED ADDED TOGETHER?????????
						starting_x = (int(self._data[command_index + 1] << 8) + int(self._data[command_index + 2])) >> 4
						ending_x = int((self._data[command_index + 2] & 0b00001111) << 8) + int(self._data[command_index + 3]) + 1
						starting_y = (int(self._data[command_index + 4] << 8) + int(self._data[command_index + 5])) >> 4
						ending_y = int((self._data[command_index + 5] & 0b00001111) << 8) + int(self._data[command_index + 6]) + 1

						self.image_display_area = Rectangle(starting_x, starting_y, ending_x - starting_x, ending_y - starting_y)
					command_index += 7
				elif command == SubPicture.DisplayControlCommand.SetPixelDataAddress.value: # 6
					image_top_field_data_address = get_endian_word(self._data, command_index + 1) + self._pixel_data_address_offset
					image_bottom_field_data_address = get_endian_word(self._data, command_index + 3) + self._pixel_data_address_offset
					command_index += 5
				elif command == SubPicture.DisplayControlCommand.ChangeColorAndContrast.value: # 7
					command_index += 1
					#int parameterAreaSize = (int)Helper.GetEndian(_data, command_index, 2)
					if command_index + 1 < len(self._data):
						parameter_area_size = self._data[command_index + 1] # this should be enough??? (no larger than 255 bytes)
						if (color_look_up_table is not None):
							# TODO: Set four_colors
							pass
						command_index += parameter_area_size
					else:
						command_index+=1
				else:
					command_index+=1
				if command_index >= len(self._data): # in case of bad files...
					break

				command = self._data[command_index]

			last_display_control_sequence_table_address = display_control_sequence_table_address
			if self._pixel_data_address_offset == -4:
				display_control_sequence_table_address = get_endian_word(self._data, command_index + 3)
			else:
				display_control_sequence_table_address = get_endian_word(self._data, display_control_sequence_table_address + 2)

		if create_bitmap and not bitmap_generated: # StopDisplay not needed (delay will be zero - should be just before start of next subtitle)
			bmp = self.generate_bitmap(self.image_display_area, image_top_field_data_address, image_bottom_field_data_address, four_colors, crop)

		# This is commented out because it interferes with some stuff. No idea how, don't care to figure it out right now
		# if bmp is not None:
			# bmp['duration'] = self.duration

		return bmp

	@staticmethod
	def set_color(
		four_colors: list[list],
		four_color_index: int,
		clut_index: int,
		color_look_up_table: list[list]
	) -> None:

		if clut_index >= 0 and clut_index < len(color_look_up_table) and four_color_index >= 0:
			four_colors[four_color_index] = copy.deepcopy(color_look_up_table[clut_index])
		return four_colors

	def generate_bitmap(
		self,
		image_display_area: Rectangle,
		image_top_field_data_address: int,
		image_bottom_field_data_address: int,
		four_colors: list[list],
		crop: bool
	):

		global alphaThreshold

		if image_display_area.width <= 0 and image_display_area.height <= 0:
			return False

		for c in range(len(four_colors)):
			if len(four_colors[c]) < 4:
				# No transparency value! Just give it 255
				four_colors[c].append(255)


		img = generateImageList(image_display_area.width, image_display_area.height, 4)	# This is a bit broken, some subtitles don't work right!


		img = self.generate_fast_bitmap(self._data, img, 0, image_top_field_data_address, four_colors)
		img = self.generate_fast_bitmap(self._data, img, 1, image_bottom_field_data_address, four_colors)


		# Start these in reverse! We'll correct them later.
		minY = len(img)
		maxY = 0
		minX = len(img[0])
		maxX = 0

		newImage = []

		# Reprocess and copy image to new array
		for y in range(len(img)):
			row = []
			# Rows
			hasContent = False
			for x in range(len(img[y])):
				# Columns
				if img[y][x][3] <= alphaThreshold:
					# Color is alpha! Knock it out.
					row.append(0)
					continue
				else:
					hasContent = True
					# Adjust X crop data
					if x < minX:
						minX = x
					if x > maxX:
						maxX = x
				row.append(img[y][x])
			if hasContent == False:
				newImage.append(0)
				continue
			else:
				newImage.append(copy.deepcopy(row))

				# Adjust Y crop data
				if y < minY:
					minY = y
				if y > maxY:
					maxY = y

		if crop == True:
			# Crop the image data
			newImage = newImage[minY:maxY + 1]

			for y in range(len(newImage)):
				if type(newImage[y]) is not list:
					# Line is alpha, do not change
					continue
				newImage[y] = newImage[y][minX:maxX + 1]

		xWidth = 0
		for row in newImage:
			if row == 0:
				continue
			if len(row) > xWidth:
				xWidth = len(row)

		parsedImage = {
			'imageData'		: newImage,
			'startTime'		: -1,
			'duration'		: round(self.delay.total_seconds(), 3), # Seconds
			'endTime'		: -1,
			'width'			: xWidth,
			'height'		: len(newImage),
			'marginTop'		: self.image_display_area.y + minY,
			'marginLeft'	: self.image_display_area.x + minX,
#			'marginRight'	: -1,
#			'marginBottom'	: -1,
		}

		return parsedImage

	@staticmethod
	def generate_fast_bitmap(
		data: bytes,
		img: list,
		startY: int,
		data_address: int,
		four_colors: list[list],
	) -> None:
		index = 0
		only_half = False
		y = startY
		x = 0
		img_height = len(img)
		img_width = len(img[0])

		while y < img_height and data_address + index + 2 < len(data):
			sup_index, run_length, color, only_half, rest_of_line = SubPicture.decode_rle(data_address + index, data, only_half)
			index += sup_index
			if rest_of_line:
				run_length = img_width - x

			for i in range(run_length):
				if x >= img_width - 1:
					# Last pixel in the row
					if y < img_height and x < img_width:
						img[y][x] = four_colors[color]

					if only_half:
						only_half = False
						index+=1
					x = 0
					y += 2	# Images are interlaced, so do every other line
					break
				if y < img_height:
					# All but the last pixel
					img[y][x] = four_colors[color]
				x += 1

		return img

	@staticmethod
	def decode_rle(
		index: int,
		data: bytes,
		only_half: bool
	) -> int:
		#Value	  Bits   n=length, c=color
		#1-3		4	  nncc			   (half a byte)
		#4-15	   8	  00nnnncc		   (one byte)
		#16-63	 12	  0000nnnnnncc	   (one and a half byte)
		#64-255	16	  000000nnnnnnnncc   (two bytes)
		# When reaching EndOfLine, index is byte aligned (skip 4 bits if necessary)
		rest_of_line = False
		b1 = data[index]
		b2 = data[index + 1]

		if only_half:
			b3 = data[index + 2]
			b1 = ((b1 & 0b00001111) << 4) | ((b2 & 0b11110000) >> 4)
			b2 = ((b2 & 0b00001111) << 4) | ((b3 & 0b11110000) >> 4)

		if b1 >> 2 == 0:
			run_length = (b1 << 6) | (b2 >> 2)
			color = b2 & 0b00000011
			if run_length == 0:
				# rest of line + skip 4 bits if Only half
				rest_of_line = True
				if only_half:
					only_half = False
					return 3, run_length, color, only_half, rest_of_line
			return 2, run_length, color, only_half, rest_of_line

		if b1 >> 4 == 0:
			run_length = (b1 << 2) | (b2 >> 6)
			color = (b2 & 0b00110000) >> 4
			if only_half:
				only_half = False
				return 2, run_length, color, only_half, rest_of_line
			only_half = True
			return 1, run_length, color, only_half, rest_of_line

		if b1 >> 6 == 0:
			run_length = b1 >> 2
			color = b1 & 0b00000011
			return 1, run_length, color, only_half, rest_of_line

		run_length = b1 >> 6
		color = (b1 & 0b00110000) >> 4

		if only_half:
			only_half = False
			return 1, run_length, color, only_half, rest_of_line
		only_half = True
		return 0, run_length, color, only_half, rest_of_line

class VobSubMergedPack: #IBinaryParagraphWithPosition
	global use_sub_timestamps

	def __init__(self, sub_picture_data: bytearray, presentation_time_stamp: timedelta, stream_id: int = False, idx_line = False):
		self.sub_picture = SubPicture(sub_picture_data)
		self.end_time = timedelta()

		if use_sub_timestamps == False or presentation_time_stamp == False:
			self.start_time = idx_line.start_time
		else:
			self.start_time = presentation_time_stamp

		self.stream_id = stream_id
		self.idx_line = idx_line

	def is_forced(self):
		return self.sub_picture.forced

	def get_bitmap(self):
#		print('-----------------------------')
#		print(self.idx_line.start_time)
#		print(self.presentation_time_stamp)
#		print('-----------------------------')
#
#		return self.sub_picture.get_bitmap(self.palette, Color("red"), Color("black"), Color("white"), Color("black"), False, True)

#		return self.sub_picture.get_bitmap(self.palette, Color("cyan"), Color("green"), Color("white"), Color("black"), False, True)
		return self.sub_picture.get_bitmap(self.palette, [0, 255, 255 ], [ 0, 255, 0 ], [ 255, 255, 255 ], [ 0, 0, 0 ], False, True)

#		return self.sub_picture.get_bitmap(self.palette, Color.Transparent, Color("black"), Color("white"), Color("black"), False, True)

	def get_position(self) -> Tuple:
		return self.sub_picture.image_display_area.x, self.sub_picture.image_display_area.y

def process_pack(id_pack: int, pack: VobSubMergedPack, folder_path: Path, palette: List[str]) -> Tuple[Path, str]:
	img = extract_subtitle_image_from_pack(pack, palette)

	img['startTime'] = round(timeToSeconds(str(pack.start_time)), 3)
	img['endTime'] = round(img['startTime'] + img['duration'], 3)

	return img

def create_subfile_text(pack_id, pack: VobSubMergedPack, image_path: Path):
	return f"{pack_id + 1}\n" + \
		f"{timeToSeconds(pack.start_time)} --> {timeToSeconds(pack.end_time)}\n" + \
		f"{image_path}\n\n"

def areColorsTheSame(color1, color2):
	# This function is intended to compare colors in the format of a list
	# [ r, g, b, a ]
	# Values are 0 to 255

	if len(color1) != len(color2):
		return False

	for i in range(len(color1)):
		if color1 != color2:
			return False

	return True

def convertPalette(palette):
	# Strip out unnecessary characters...
	for i in range(len(palette)):
		palette[i] = palette[i].strip('#').strip()
		palette[i] = [ int(palette[i][0:2], 16), int(palette[i][2:4], 16), int(palette[i][4:6], 16) ]

	return palette

def extract_subtitle_image_from_pack(pack: VobSubMergedPack, palette: List[str]):
	pack.palette = palette

	img = pack.get_bitmap()

	return img

def ssaSubpictureHeader(videoCroppedWidth, videoCroppedHeight):
	global scriptVersion
	return """[Script Info]
; Script generated by Sub2Ass.py version """ + scriptVersion + """
ScriptType: v4.00+
PlayResX: """ + str(videoCroppedWidth) + """
PlayResY: """ + str(videoCroppedHeight) + """
ScaledBorderAndShadow: no
YCbCr Matrix: None"""

def checkPixels(pixel1, pixel2):
	if type(pixel1) is list and type(pixel2) is list:
		if len(pixel1) != len(pixel2):
			return False
		for i in range(len(pixel1)):
			if pixel1[i] != pixel2[i]:
				return False
	return True

def getRepeatPixelCount(pixelRow, start, charList):
	# charList is the list of 'blocks' or 'spaces' in pixelFont we are using
	count = 1
	pos = start
	while pos < len(pixelRow) and count <= len(charList):
		if type(pixelRow[pos]) is not type(pixelRow[start]):
			break
		if type(pixelRow[pos]) is list:
			if not areSubpictureColorsTheSame(pixelRow[start], pixelRow[pos]):
				break

		count += 1
		pos += 1
	return count - 1

def areSubpictureColorsTheSame(color1, color2):
	if type(color1) != type(color2):
		return False
	if type(color1) is not list:
		return False
	for i in range(3):
		if color1[i] != color2[i]:
			return False
	return True

def findColor(colorList, foundColor):
	i = 0
	while i < len(colorList):
		if areSubpictureColorsTheSame(colorList[i], foundColor):
			return i
		i += 1
	colorList.append(foundColor)
	return i

def imageToass(imageData, colorList):
	currentColor = []
	emptyLines = 0	# Using this keeps gaps to a minimum, and also knocks out tailing empty lines

	# This is just used as a pointer to make a few things cleaner below
	charList = pixelFont['spaces']

	foundData = False

	output = ''
	if type(imageData) is not list:
		return ''
	for y in range(len(imageData)):
		if type(imageData[y]) is not list:
			if foundData == False:
				# We haven't even found a single pixel yet, there's no point in having blank lines at the start!
				continue
			# Row is empty, skip
			if maxEmptyLines < 0 or emptyLines < maxEmptyLines:
				emptyLines += 1
			continue

		if foundData == True:
			# Add a newline to all but the first line
			output += '\\N'
			emptyLines = max(0, emptyLines - 1)
		if emptyLines > 0:
			while emptyLines > 0:
				output += pixelFont['spaces'][0] + '\\N'
				emptyLines -= 1

		foundData = True
		emptyLines = 0

		x = 0
		while x < len(imageData[y]):
			currentPixel = imageData[y][x]
			if type(currentPixel) is not list or currentPixel[3] < alphaThreshold:
				# Transparent pixel(s)
				charList = pixelFont['spaces']
			else:
				# Visible pixel(s)
				charList = pixelFont['blocks']

				# Check to see if we need to change color
				if len(currentColor) == 0 or not areSubpictureColorsTheSame(currentColor, currentPixel):
					# Need to add color info!
					styleIndex = findColor(colorList, currentPixel)
					if styleIndex == 0:
						if len(currentColor) == 0 and areSubpictureColorsTheSame(colorList[0], currentPixel):
							# This is the first color. Leave it blank, it will be the default style color anyway
							pass
						else:
							# New color is just the default color
							output += '{\\r}'
					else:
						output += '{\\r' + intToHex(styleIndex) + '}'
#						output += '{\\c&H' + intColorToHexColor(currentPixel[2]) + intColorToHexColor(currentPixel[1]) + intColorToHexColor(currentPixel[0]) + '&,\\3c&H' + intColorToHexColor(currentPixel[2]) + intColorToHexColor(currentPixel[1]) + intColorToHexColor(currentPixel[0]) + '&}'
					currentColor = copy.deepcopy(currentPixel[0:3])

			repetitions = getRepeatPixelCount(imageData[y], x, charList)
			output += charList[repetitions - 1]
			x += repetitions

	return { 'colorList' : colorList, 'imageData' : output }

def areImageBitmapsTheSame(image1, image2):
	if len(image1) != len(image2):
		return False

	for y in range(len(image1)):

		if type(image1[y]) is not type(image2[y]):
			return False
		if type(image1[y]) is not list:
			if type(image2[y]) is not list:
				continue
			else:
				return False

		if len(image1[y]) != len(image2[y]):
			return False
		for x in range(len(image1)):

			if type(image1[y][x]) is not type(image2[y][x]):
				return False
			if type(image1[y][x]) is not list:
				if type(image2[y][x]) is not list:
					continue
				else:
					return False

			if len(image1[y][x]) != len(image2[y][x]):
				return False
			for c in range(len(image1[y][x])):
				if image1[y][x][c] != image2[y][x][c]:
					return False

	return True

def multiprocess(_vob_sub_merged_pack_list, outputFilePath, _palette, n_jobs, timeAdjustmentFactor, timeOffset, videoWidth, videoHeight, videoCropData):
	global alignmentThreshold
	global alpha_threshold

	global maxSubtitleDuration
	global imageHeightThreshold
	global imageWidthThreshold

	global resolutionScale
	global fontHeight
	global minMargin

	image_paths = []
	subfile_texts = []
	multi_process_pack = partial(process_pack, folder_path=outputFilePath, palette=_palette)
	num_packs = len(_vob_sub_merged_pack_list)


	# Parse the crop data into something useful!
	videoCropData = videoCropData.split(':')
	for c in range(len(videoCropData)):
		videoCropData[c] = int(videoCropData[c])

	# videoCropData[0] = total width
	# videoCropData[1] = total height
	# videoCropData[2] = x position
	# videoCropData[3] = y position

	cropLeft = videoCropData[2]
	cropRight = videoWidth - videoCropData[2] - videoCropData[0]
	cropTop = videoCropData[3]
	cropBottom = videoHeight - videoCropData[3] - videoCropData[1]

	alignmentTotals = {
		'1' : 0,
		'2' : 0,
		'3' : 0,
		'4' : 0,
		'5' : 0,
		'6' : 0,
		'7' : 0,
		'8' : 0,
		'9' : 0
	}

	mostCommonAlignment = 2	# Placeholder value, we will fix it later

	colorList = []

	outputSubtitles = []

	# If there is already a .ass file, delete it
	if os.path.exists(outputFilePath):
		os.remove(outputFilePath)

	with open(outputFilePath, 'w') as subFile:
		subFile.write(ssaSubpictureHeader(int(videoCropData[0] * resolutionScale), int(videoCropData[1] * resolutionScale)))

		pixelHeightsPerLine = []

		finishedCount = 0
		previousPercentage = 0

		with concurrent.futures.ProcessPoolExecutor(n_jobs) as executor:
			subtitleList = []
			print()
			displayProgress(0, 1, 0, len(range(num_packs)))

			results = []
			for result in executor.map(
					multi_process_pack, range(num_packs), _vob_sub_merged_pack_list
				):

				results.append(result)

				finishedCount += 1
				percentage = round(finishedCount / num_packs * 100, 1)
				if percentage != previousPercentage:
					displayProgress(percentage, 1, finishedCount, len(range(num_packs)))
					previousPercentage = percentage

			previousPercentage = 0
			maxHeight = 0
			maxWidth = 0

			results.sort(key=lambda results: results['startTime'])

			displayProgress(0, 2, 0, len(range(num_packs)))

			i = -1
			while i + 1 < len(results):
				i += 1

				percentage = round(i / len(results) * 100, 1)
				if percentage != previousPercentage:
					displayProgress(percentage, 2, i, len(results))
					previousPercentage = percentage

				result = results[i]

				if result == False:
					# For some reason, the image was blank. Continue on, nothing to see here!
					continue

				# Finish calculating the remaining data we need
				result['frameWidth']	= videoWidth
				result['frameHeight']	= videoHeight
				result['marginRight']	= videoWidth - result['marginLeft'] - result['width']
				result['marginBottom']	= videoHeight - result['marginTop'] - result['height']

				result['alignment'] = 5
				if result['marginBottom'] / videoHeight < alignmentThreshold or result['marginTop'] - result['marginBottom'] > alignmentThreshold * videoHeight:
					result['alignment'] -= 3
				elif result['marginTop'] / videoHeight < alignmentThreshold or result['marginTop'] - result['marginBottom'] < alignmentThreshold * videoHeight * -1:
					result['alignment'] += 3
				if result['marginLeft'] / videoWidth < alignmentThreshold and result['marginLeft'] - result['marginRight'] > alignmentThreshold * videoWidth:
					result['alignment'] -= 1
				elif result['marginRight'] / videoWidth  < alignmentThreshold and result['marginLeft'] - result['marginRight'] < alignmentThreshold * videoWidth * -1:
					result['alignment'] += 1

				if result['alignment'] > 3 and result['alignment'] < 7:
					# If the subtitle is in the vertical center row, drop it down to the bottom row. We don't need it in the middle of the video!
					result['alignment'] = result['alignment'] - 3

				alignmentTotals[str(result['alignment'])] += 1

				addSubtitle = True

				if result['startTime'] == -1 or result['endTime'] == -1:
					# -1 means the time is invalid. Skip on ahead, there's no way to use this subtitle
					addSubtitle = False

					match = False
					while i + 1 < len(results) and result['endTime'] + 0.1 > results[i + 1]['startTime'] and areImageBitmapsTheSame(result['imageData'], results[i + 1]['imageData']):
						# Subtitle is followed by one or more duplicates! Increase the index to ignore the duplicates
						match = True
						i += 1
					if match == True:
						result['endTime'] = results[i]['endTime']

				if result['startTime'] + 0.075 >= result['endTime']:
					# Duration is too short or invalid!
					if i < len(results) - 1:
						# If there is no duration data, use the next subtitle start time and hope it works well enough
						result['endTime'] = results[i + 1]['startTime']
					else:
						# This is the last subtitle in the video. Just make it maxSubtitleDuration seconds long, since we have no idea otherwise
						result['endTime'] = result['startTime'] + maxSubtitleDuration

				subWidth = 0
				for a in range(len(result['imageData'])):
					if type(result['imageData'][a]) is list:
						subWidth = max(subWidth, len(result['imageData'][a]))
						break
				if len(result['imageData']) < imageHeightThreshold and subWidth < imageWidthThreshold:
					# Image is too small. Probably just a placeholder for removing a subtitle. Ignore it
					continue

				if result['startTime'] + maxSubtitleDuration < result['endTime']:
					# Restrict maximum subtitle length to maxSubtitleDuration seconds, nothing should be longer than that
					result['endTime'] = result['startTime'] + maxSubtitleDuration

				if i < len(results) - 1:
					# If this subtitle overlaps the next one, terminate it at that time
					if result['endTime'] >= results[i + 1]['startTime']:
						result['endTime'] = results[i + 1]['startTime']

				if addSubtitle == True:
					# Do some extra calculating to use for dynamic sizing
					currentLineHeight = 0
					foundLine = False
					for image in result['imageData']:
						if type(image) is list:
							maxWidth = max(maxWidth, len(image))	# Get the width to use in maxWidth
							if foundLine == True:
								currentLineHeight += 1
							else:
								foundLine = True
								currentLineHeight = 1
						else:
							if foundLine == True:
								if currentLineHeight >= imageHeightThreshold:	# MAKE SURE to use imageHeightThreshold to discard anything too small
									pixelHeightsPerLine.append(currentLineHeight)
								foundLine = False
					if foundLine == True and currentLineHeight >= imageHeightThreshold:
						pixelHeightsPerLine.append(currentLineHeight)
					pixelHeightsPerLine.append(currentLineHeight)


					alignment = ''
					if keepPosition == True:
						if result['alignment'] != mostCommonAlignment:
							alignment = '{\\an' + str(result['alignment']) + '}'

					position = ''
					parsedEntry = imageToass(result['imageData'], colorList)

					colorList = parsedEntry['colorList']

					outputSubtitles.append({
						'startTime'	: secondsToTime(max(0, (result['startTime'] * timeAdjustmentFactor) + (timeOffset))),
						'endTime'	: secondsToTime(max(0, (result['endTime']  *  timeAdjustmentFactor) + (timeOffset))),
						'text'		: alignment + position + parsedEntry['imageData'],
					})

					# This has to be done here, because we cut out dead space between lines
					maxHeight = max(maxHeight, parsedEntry['imageData'].count('\\N') + 1)

			displayProgress(100, 2, len(results), len(results))

		# Calculate the font size! Try to get as close to the user's desired value without truncating anything
		averageLineHeight = 0
		for l in range(len(pixelHeightsPerLine)):
			averageLineHeight += pixelHeightsPerLine[l]
		averageLineHeight /= len(pixelHeightsPerLine)

		# Truncate this to one decimal point
		averageLineHeight = int(averageLineHeight * 10) / 10

		fontSize = fontHeight / averageLineHeight

		# Set the maximum font size to a size that stays within the video boundaries
		fontSize = min((videoCropData[0] - (minMargin * 2)) / maxWidth, fontSize)	# Remember to include Right/Left margins
		fontSize = min((videoCropData[1] - minMargin) / maxHeight, fontSize)	# Remember to include bottom margin, there is no top margin

		# Truncate to three decimal points
		fontSize = int(fontSize * 1000) / 1000

		# Add the color styles
		subFile.write('\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding')
		for c in range(len(colorList)):
			newStyle = []

			newStyle.append(str(c))	# Style name
			newStyle.append(fontName)	# Font name
			newStyle.append(str(fontSize * resolutionScale))	# Font size
			newStyle.append(intColorToAssColor(colorList[c]))	# Primary Color
			newStyle.append(intColorToAssColor(colorList[c]))	# Secondary Color
			newStyle.append(intColorToAssColor(colorList[c]))	# Outline Color
#			newStyle.append(intColorToAssColor([ 0, 0, 0, 207 ]))	# Back Color	# I THINK THE SLIGHT TRANSPARENCY IS CAUSING SOME LAG ON MOBILE DEVICES
			newStyle.append(intColorToAssColor([ 0, 0, 0, 255 ]))	# Back Color
			newStyle.append('0')	# Bold
			newStyle.append('0')	# Italic
			newStyle.append('0')	# Underline
			newStyle.append('0')	# Strikeout
			newStyle.append('100')	# Scale X
			newStyle.append('100')	# Scale Y
			newStyle.append('0')	# Spacing
			newStyle.append('0')	# Angle
			newStyle.append('1')	# Border Style
			newStyle.append('0.05')	# Outline -- This value prevents lines from showing up between pixels, DO NOT REMOVE
			newStyle.append(str(shadowSize))	# Shadow
			newStyle.append(str(mostCommonAlignment))	# Alignment
			newStyle.append(str(minMargin))	# MarginL
			newStyle.append(str(minMargin))	# Margin R
			newStyle.append(str(minMargin))	# Margin V
			newStyle.append('1')	# Encoding

			subFile.write('\nStyle: ' + ','.join(newStyle))

		# Add the events
		subFile.write('\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text')
		for entry in outputSubtitles:
			subFile.write('\nDialogue: 0,' + entry['startTime'] + ',' + entry['endTime'] + ',0,,0,0,0,,' + entry['text'])

	print(cursorControl.up + cursorControl.eraseRemaining + colors.white + 'Finished!\n\n' + colors.none + 'Wrote: ' + colors.blue + outputFilePath + '\n\n' + colors.red + 'Remember to attach the font file for ' + colors.white + fontName + colors.red + ' inside your final MKV file!\n' + colors.none)

	return True

def is_mpeg2_pack_header(buffer: bytearray) -> bool:
	return len(buffer) >= 4 \
			and buffer[0] == 0 \
			and buffer[1] == 0 \
			and buffer[2] == 1 \
			and buffer[3] == 0xba; # 0xba == 186 - MPEG-2 Pack Header

def is_private_stream1(buffer: bytearray, index: int) -> bool:
	return len(buffer) >= index + 4 \
			and buffer[index + 0] == 0 \
			and buffer[index + 1] == 0 \
			and buffer[index + 2] == 1 \
			and buffer[index + 3] == 0xbd; # 0xbd == 189 - MPEG-2 Private stream 1 (non MPEG audio, subpictures)

def is_private_stream2(buffer: bytearray, index: int) -> bool:
	return len(buffer) >= index + 4 \
			and buffer[index + 0] == 0 \
			and buffer[index + 1] == 0 \
			and buffer[index + 2] == 1 \
			and buffer[index + 3] == 0xbf; # 0xbf == 191 - MPEG-2 Private stream 2

def is_subtitle_pack(buffer: bytearray) -> bool:
	if is_mpeg2_pack_header(buffer) and is_private_stream1(buffer, Mpeg2Header.LENGTH):
		pesHeader_data_length = buffer[Mpeg2Header.LENGTH + 8]
		streamId = buffer[Mpeg2Header.LENGTH + 8 + 1 + pesHeader_data_length]

		return streamId >= 0x20 and streamId <= 0x3f # Subtitle IDs allowed (or x3f to x40?)
	return False

class Mpeg2Header:
	#  <summary>
	#  http://www.mpucoder.com/DVD/packhdr.html
	#  </summary>
	LENGTH = 14

	def __init__(self, buffer: bytes):

		self.start_code = get_endian(buffer, 0, 3)
		self.pack_identifier = buffer[3]
		self.program_mux_rate = get_endian(buffer, 10, 3) >> 2
		self.pack_stuffing_length = buffer[13] & 0b00000111

class PacketizedElementaryStream:
	HEADER_LENGTH: int = 6

	def __init__(self, buffer: bytearray, index: int):
		self.buffer = buffer
		self.start_code = get_endian(buffer, index, 3)
		self.stream_id = buffer[index + 3]
		self.length = get_endian_word(buffer, index + 4)

		self.scrambling_control = (buffer[index + 6] >> 4) & 0b00000011
		self.priority = buffer[index + 6] & 0b00001000
		self.data_alignment_indicator = buffer[index + 6] & 0b00000100
		self.copyright = buffer[index + 6] & 0b00000010
		self.original_or_copy = buffer[index + 6] & 0b00000001
		self.presentation_timestamp_decode_timestamp_flags = buffer[index + 7] >> 6
		self.elementary_stream_clock_reference_flag = buffer[index + 7] & 0b00100000
		self.es_rate_flag = buffer[index + 7] & 0b00010000
		self.dsm_trick_mode_flag = buffer[index + 7] & 0b00001000
		self.additional_copy_info_flag = buffer[index + 7] & 0b00000100
		self.crc_flag = buffer[index + 7] & 0b00001000
		self.extension_flag = buffer[index + 7] & 0b00000010

		self.header_data_length = buffer[index + 8]

		if self.stream_id == 0xBD:
			id = buffer[index + 9 + self.header_data_length]
			if id >= 0x20 and id <= 0x40: # x3f 0r x40 ?
				self.sub_picture_stream_id = id

		temp_index = index + 9
		if self.presentation_timestamp_decode_timestamp_flags == 0b00000010 or \
			self.presentation_timestamp_decode_timestamp_flags == 0b00000011:

			self.presentation_timestamp = buffer[temp_index + 4] >> 1 #ulong
			self.presentation_timestamp += buffer[temp_index + 3] << 7
			self.presentation_timestamp += (buffer[temp_index + 2] & 0b11111110) << 14
			self.presentation_timestamp += buffer[temp_index + 1] << 22
			self.presentation_timestamp += (buffer[temp_index + 0] & 0b00001110) << 29

			temp_index += 5
		if self.presentation_timestamp_decode_timestamp_flags == 0b00000011:
			self.decode_timestamp = buffer[temp_index + 4] >> 1
			self.decode_timestamp += buffer[temp_index + 3] << 7
			self.decode_timestamp += (buffer[temp_index + 2] & 0b11111110) << 14
			self.decode_timestamp += buffer[temp_index + 1] << 22
			self.decode_timestamp += (buffer[temp_index + 0] & 0b00001110) << 29

		data_index = index + self.header_data_length + 24 - Mpeg2Header.LENGTH

		data_size = self.length - (4 + self.header_data_length)

		if data_size < 0 or (data_size + data_index > len(buffer)): #// to fix bad subs...
			self.data_size = len(buffer) - data_index
			if (self.data_size < 0):
				return

		self._data_buffer = buffer[data_index:data_index+data_size]

	def write_to_stream(self, stream: bytes):
		return stream + self._data_buffer

def getFileExtension(inputFile):
	if not '.' in inputFile:
		return inputFile
	temp = inputFile.rsplit('.', 1)
	return temp[-1]

def removeFileExtension(inputFile):
	if not '.' in inputFile:
		return inputFile
	temp = inputFile.rsplit('.', 1)
	return temp[0]

class VobSubParser:
	def __init__(self, is_pal: bool):
		self.is_pal = is_pal
		self.vob_sub_packs: list[VobSubPack] = []
#		self.settings = SettingsArgs()

	def open_file(self, filename: str) -> None:
		with open(filename, mode='rb') as file:
			return file

	# /// <summary>
	# /// Can be used with e.g. MemoryStream or FileStream
	# /// </summary>
	# /// <param name="ms"></param>
	def open(self, ms: bytes):
		ms.Position = 0
		# var buffer = new byte[0x800] // 2048
		position = 0
		while (position < len(ms)):
			self.vob_sub_packs = []
			ms.seek(position, 0)
			buffer = ms.read(0x0800)
			if (is_subtitle_pack(buffer)):
				self.vob_sub_packs.append(VobSubPack(buffer, None))

			position += 0x800

	def open_json_subs(self, jsonData):
		subtitles = jsonData['subpictures']

		list_vob_sub_merge_pack = []

		for x in range(len(subtitles)):
			subtitles[x]['data'] = bytes.fromhex(subtitles[x]['data'])

			list_vob_sub_merge_pack.append(VobSubMergedPack(subtitles[x]['data'], timedelta(seconds=subtitles[x]['startTime'])))

		# Fix subs with no duration (completely normal) or negative duration or duration > 10 seconds
		for i in range(len(list_vob_sub_merge_pack)):
			pack = list_vob_sub_merge_pack[i]

			if pack.sub_picture.delay.total_seconds() * 1000 > 0:
				pack.end_time = pack.start_time + pack.sub_picture.delay

			if pack.end_time < pack.start_time \
				or pack.end_time.total_seconds() * 1000 - pack.start_time.total_seconds() * 1000 \
					> subtitle_maximum_display_milliseconds:

				if i + 1 < len(list_vob_sub_merge_pack):

					pack.end_time = timedelta(
						seconds=((list_vob_sub_merge_pack[i + 1].start_time.total_seconds() * 1000 \
						- minimum_milliseconds_between_lines) / 1000)
					)

					if pack.end_time.total_seconds() * 1000 - pack.start_time.total_seconds() * 1000 \
						> subtitle_maximum_display_milliseconds:

						pack.end_time = timedelta(seconds=((pack.start_time.total_seconds() * 1000 \
							+ subtitle_maximum_display_milliseconds) / 1000)
						)
					else:
						pack.end_time = timedelta(seconds=((pack.start_time.total_seconds() * 1000 + 3000) / 1000))

			self.vob_sub_packs.append(list_vob_sub_merge_pack[i])

		return self.vob_sub_packs

	def open_sub_idx(self, vob_sub_filename: str,  idx_filename: str):
		self.vob_sub_packs = []
		if not os.path.exists(idx_filename):
			# // No valid idx file found - just open like vob file
			self.open_file(vob_sub_filename)
			use_sub_timestamps = True
			return
		idx = Idx(idx_filename)
		self.idx_palette = idx.palette
		self.idx_languages = idx.languages
		if len(idx.idx_paragraphs) > 0:
			with open(vob_sub_filename, mode='rb') as fs:
				file = fs.read()
				for p in idx.idx_paragraphs:
					if p.file_position + 100 < len(file):
						position = p.file_position
						# fs.seek(p.file_position, 0)
						buffer = file[position: position + 0x0800]
						if is_subtitle_pack(buffer) or is_private_stream1(buffer, 0):
							vsp = VobSubPack(buffer, p)
							self.vob_sub_packs.append(vsp)
							if is_private_stream1(buffer, 0):
								position += vsp.packetized_elementary_stream.length + 6
							else:
								position += 0x800

							current_sub_picture_stream_id = 0
							if vsp.packetized_elementary_stream.sub_picture_stream_id != None:
								current_sub_picture_stream_id = vsp.packetized_elementary_stream.sub_picture_stream_id #.Value ?

							while vsp.packetized_elementary_stream != None \
								and hasattr(vsp.packetized_elementary_stream, 'sub_picture_stream_id') \
								and (vsp.packetized_elementary_stream.length == PES_MAX_LENGTH \
									or current_sub_picture_stream_id != vsp.packetized_elementary_stream.sub_picture_stream_id) \
								and position < len(file):

								# fs.seek(position, 0)
								# buffer = fs.read(0x800)
								buffer = file[position: position + 0x0800]
								vsp = VobSubPack(buffer, p) # idx position?

								if vsp.packetized_elementary_stream is not None \
									and hasattr(vsp.packetized_elementary_stream, 'sub_picture_stream_id') \
									and current_sub_picture_stream_id == vsp.packetized_elementary_stream.sub_picture_stream_id:
									self.vob_sub_packs.append(vsp)

									if is_private_stream1(buffer, 0):
										position += vsp.packetized_elementary_stream.length + 6
									else:
										position += 0x800
								else:
									position += 0x800
									fs.seek(position, 0)
			return

	def merge_vob_sub_packs(self) -> List[VobSubMergedPack]:
		"""
		Demultiplex multiplexed packs together each stream_id at a time + removing bad packs + fixing displaytimes
		:return: List of complete packs each with a complete sub image
		"""
		list_vob_sub_merge_pack: List[VobSubMergedPack] = []
		ms = bytearray()

		ticks_per_millisecond = 90.000
		if not self.is_pal:
			ticks_per_millisecond = 90.090 * (23.976 / 24)

		# get unique stream_ids
		unique_stream_ids = []
		for p in self.vob_sub_packs:
			if p.packetized_elementary_stream is not None \
				and hasattr(p.packetized_elementary_stream, "sub_picture_stream_id") \
				and p.packetized_elementary_stream.sub_picture_stream_id not in unique_stream_ids:

				unique_stream_ids.append(p.packetized_elementary_stream.sub_picture_stream_id)

		last_idx_paragraph: IdxParagraph = None
		for unique_stream_id in unique_stream_ids: # packets must be merged in stream_id order (so they don't get mixed)
			for p in self.vob_sub_packs:
				if (p.packetized_elementary_stream is not None  \
					and hasattr(p.packetized_elementary_stream, "sub_picture_stream_id") \
					and p.packetized_elementary_stream.sub_picture_stream_id == unique_stream_id):

					if p.packetized_elementary_stream.presentation_timestamp_decode_timestamp_flags > 0:
						if last_idx_paragraph is None or p.idx_line.file_position != last_idx_paragraph.file_position:
							if len(ms) > 0:
								list_vob_sub_merge_pack.append(VobSubMergedPack(ms, pts, stream_id, last_idx_paragraph))

							ms = bytearray()
							pts = timedelta(seconds = float(p.packetized_elementary_stream.presentation_timestamp / ticks_per_millisecond) / 1000) # 90000F * 1000)); (PAL)
							stream_id = p.packetized_elementary_stream.sub_picture_stream_id
					last_idx_paragraph = p.idx_line
					ms = p.packetized_elementary_stream.write_to_stream(ms)
			if len(ms) > 0:
				list_vob_sub_merge_pack.append(VobSubMergedPack(ms, pts, stream_id, last_idx_paragraph))
				ms = bytearray()

		# Remove any bad packs
		for i in range(len(list_vob_sub_merge_pack))[::-1]:
			pack = list_vob_sub_merge_pack[i]
			if pack.sub_picture == None \
				or pack.sub_picture.image_display_area.width <= 3 \
				or pack.sub_picture.image_display_area.height <= 2:

				list_vob_sub_merge_pack.pop(i)

			elif pack.end_time.total_seconds() - pack.start_time.total_seconds() < 0.1 \
				and pack.sub_picture.image_display_area.width <= 10 \
				and pack.sub_picture.image_display_area.height <= 10:

				list_vob_sub_merge_pack.pop(i)

		# Fix subs with no duration (completely normal) or negative duration or duration > 10 seconds
		for i in range(len(list_vob_sub_merge_pack)):
			pack = list_vob_sub_merge_pack[i]
			if pack.sub_picture.delay.total_seconds() * 1000 > 0:
				pack.end_time = pack.start_time + pack.sub_picture.delay

			if pack.end_time < pack.start_time \
				or pack.end_time.total_seconds() * 1000 - pack.start_time.total_seconds() * 1000 \
					> subtitle_maximum_display_milliseconds:

				if i + 1 < len(list_vob_sub_merge_pack):

					pack.end_time = timedelta(
						seconds=((list_vob_sub_merge_pack[i + 1].start_time.total_seconds() * 1000 \
						- minimum_milliseconds_between_lines) / 1000)
					)

					if pack.end_time.total_seconds() * 1000 - pack.start_time.total_seconds() * 1000 \
						> subtitle_maximum_display_milliseconds:

						pack.end_time = timedelta(seconds=((pack.start_time.total_seconds() * 1000 \
							+ subtitle_maximum_display_milliseconds) / 1000)
						)
					else:
						pack.end_time = timedelta(seconds=((pack.start_time.total_seconds() * 1000 + 3000) / 1000))
		return list_vob_sub_merge_pack

def extract_vob_sub_img_to_ass(vob_sub_file_name: Path, outputFilePath: Path, videoWidth: int, videoHeight: int, colorPalette = [], videoCropData: str = '', timeAdjustmentFactor: float = 1, timeOffset: float = 0) -> List[Path]:
	global use_sub_timestamps
	global args

	allowYUVConversion = False

	n_jobs = max(1, int(psutil.cpu_count(logical = False) * .75)) # Set the number of threads to a number relevant to our CPU core count

	if videoCropData == '':
		videoCropData = str(videoWidth) + ':' + str(videoHeight) + ':0:0'

	vob_sub_parser = VobSubParser(True)

	subFormat = getFileExtension(vob_sub_file_name).lower()

	if subFormat == 'json':
		if not os.path.exists(vob_sub_file_name):
			raise FileNotFoundError('Could not find "' + vob_sub_file_name + '" !')

		use_sub_timestamps = True

		try:
			jsonData = readJSONFile(vob_sub_file_name)
		except:
			raise Exception('Could not load JSON data from "' + vob_sub_file_name + '" ! Are you sure this is a JSON file?')

		if 'palette' in jsonData:
			if len(jsonData['palette']) == 16:
				colorPalette = jsonData['palette']
			else:
				print('Invalid color palette in JSON file!')
		elif len(colorPalette) != 16:
			raise Exception('Invalid color palette!')

		_vob_sub_merged_pack_list = vob_sub_parser.open_json_subs(jsonData)

	elif subFormat == 'idx' or subFormat == 'sub':
		if subFormat == 'idx':
			vob_sub_file_name = removeFileExtension(vob_sub_file_name)
			idx_file_name = vob_sub_file_name + '.idx'
			vob_sub_file_name += '.sub'
		else:
			idx_file_name = removeFileExtension(vob_sub_file_name) + '.idx'

		if not os.path.exists(vob_sub_file_name):
			raise FileNotFoundError('Could not find "' + vob_sub_file_name + '" !')
		if not os.path.exists(idx_file_name):
			raise FileNotFoundError('Could not find "' + idx_file_name + '" !')
		

		vob_sub_parser.open_sub_idx(str(vob_sub_file_name), str(idx_file_name))
		_vob_sub_merged_pack_list = vob_sub_parser.merge_vob_sub_packs()

		# If no palette was supplied, use the IDX file palette
		if len(colorPalette) != 16:
			colorPalette = vob_sub_parser.idx_palette
			for i in range(len(colorPalette)):
				colorPalette[i] = idxToRGB(colorPalette[i])
				allowYUVConversion = False

	for i in range(len(colorPalette)):
		colorPalette[i] = str(colorPalette[i]).strip()
		if args.convert_YUV == True and allowYUVConversion == True:
			colorPalette[i] = YUVStringToRGBString(colorPalette[i])

	colorPalette = convertPalette(colorPalette)

	return multiprocess(_vob_sub_merged_pack_list, outputFilePath, colorPalette, n_jobs, timeAdjustmentFactor, timeOffset, videoWidth, videoHeight, videoCropData)

class Idx:

	def __init__(self, file_name: str):
		self.idx_paragraphs: List[IdxParagraph] = []
		self.palette: List[str] = [] #Colour
		self.languages: List[str] = []
#		self.time_code_line_pattern = re.compile("^timestamp: \d+:\d+:\d+:\d+, filepos: [\dabcdefABCDEF]+$")


		with open(file_name) as file:
			lines = file.readlines()

		self.process_file(lines)


	def process_file(self, lines: List[str]):
		language_index = 0
		for line in lines:
			line = line.strip('\n')
			if line.find('timestamp: ') >= 0 and line.find(', filepos: ') >= 0:
#			if self.time_code_line_pattern.search(line) is not None:
				p: IdxParagraph = self.get_time_code_and_file_position(line)
				if p is not None:
					self.idx_paragraphs.append(p)

			elif line.startswith("palette:") and len(line) > 10:
				s =  line.strip('palette:').split(',')
				colors = [c.strip(' ') for c in s]
				for hex_str in colors:
					self.palette.append(self.hex_to_color(hex_str))

			elif line.startswith("id:") and len(line) > 4:
				# id: en, index: 1
				# id: es, index: 2
				self.language_index = line[-2].strip(' ')
				self.two_letter_language_id = line.split(',')[0][-3:].strip(' ')
				# parts = line.split(new[] { ':', ',', ' ' }, StringSplitOptions.RemoveEmptyEntries);
				# if parts.Length > 1:
					# string twoLetterLanguageId = parts[1];
					# string languageName = DvdSubtitleLanguage.GetLocalLanguageName(twoLetterLanguageId);
					# if (parts.Length > 3 && parts[2].Equals("index", StringComparison.OrdinalIgnoreCase))
					# {
					#	 int index;
					#	 if (int.TryParse(parts[3], out index))
					#	 {
					#		 languageIndex = index;
					#	 }
					# }
					# # Use U+200E (LEFT-TO-RIGHT MARK) to support right-to-left scripts
					# Languages.Add(string.Format("{0} \x200E(0x{1:x})", languageName, languageIndex + 32));
					# languageIndex++;


	def hex_to_color(self, hex_str: str):
		hex_str = hex_str.strip('#').strip()
		if (len(hex_str) == 6):
			r = int(hex_str[0: 2], 16)
			g = int(hex_str[2: 4], 16)
			b = int(hex_str[4: 6], 16)
			return padHexColor(hex(r).split('x').pop()) + padHexColor(hex(g).split('x').pop()) + padHexColor(hex(b).split('x').pop())


#			r = int(hex_str[0: 2], 16) / 255
#			g = int(hex_str[2: 4], 16) / 255
#			b = int(hex_str[4: 6], 16) / 255
#			return Color(rgb=(r, g, b))

		elif (len(hex_str) == 8):
			a = int(hex_str[0: 2], 16)
			r = int(hex_str[2: 4], 16)
			g = int(hex_str[4: 6], 16)
			b = int(hex_str[6: 8], 16)
			return hex(r).split('x').pop() + hex(g).split('x').pop() + hex(b).split('x').pop()

#			a = int(hex_str[0: 2], 16)
#			r = int(hex_str[2: 4], 16)
#			g = int(hex_str[4: 6], 16)
#			b = int(hex_str[6: 8], 16)
#			return Color(rgba=(r, g, b, a))
#		return Color("red")
		return 'ff00ff'

	def get_time_code_and_file_position(self, line: str) -> IdxParagraph:
		# timestamp: 00:00:01:401, filepos: 000000000
		timestamp, filepos = line.split(',')
		timestamp = timestamp[-12:]
		filepos = int(filepos[-9:], 16)
		if (len(timestamp.split(':')) == 4):
			hours, minutes, seconds, milliseconds = [int(o) for o in timestamp.split(':')]
			return IdxParagraph(timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds), filepos)
		return None

def get_endian_word(buffer: bytearray, index: int) -> int:
	"""
	Get two bytes word stored in endian order
	:param: buffer: bytearray
	:param: index: index in byte array

	"""
	if (index + 1 < len(buffer)):
		return (buffer[index] << 8) | buffer[index + 1]

	return 0

def get_endian(buffer: bytearray, index: int, count: int):
	result = 0
	for i in range(count):
		result = (result << 8) + buffer[index + i]

	return result

class VobSubPack:
		packetized_elementary_stream: PacketizedElementaryStream
		mpeg_2_header: Mpeg2Header

		def __init__(self, buffer: bytes, idx_line: IdxParagraph):
			self._buffer = buffer
			self.idx_line = idx_line

			if (is_mpeg2_pack_header(buffer)):

				self.mpeg_2_header = Mpeg2Header(buffer)
				self.packetized_elementary_stream = PacketizedElementaryStream(buffer, self.mpeg_2_header.LENGTH)

			elif (is_private_stream1(buffer, 0)):

				self.packetized_elementary_stream = PacketizedElementaryStream(buffer, 0)


parser = argparse.ArgumentParser("commands")
parser.add_argument("--input_file", required=True, help="The path to the .sub, .idx or .json file to convert.", type=str)
parser.add_argument("--output_file", required=True, help="The path to use for the .ass file output.", type=str)
parser.add_argument("--video_width", required=True, help="The width of the original video (Usually 720).", type=int)
parser.add_argument("--video_height", required=True, help="The height of the original video (Usually 480 or 576).", type=int)

parser.add_argument("--palette", required=False, default='', help="The color palette (16 RGB hexadecimal colors, delimited with commas).", type=str)
parser.add_argument("--convert_YUV", default=False, required=False, help="Optional - this will treat the --palette values as YUV, and convert them to RGB for you automatically.", type=bool)

parser.add_argument("--use_sub_timestamps", default=False, required=False, help="Optional - this will use the timestamps obtained from the VOB/SUB file, instead of from the IDX file.", type=float)

parser.add_argument("--crop_data", required=False, help="Optional - the parent video's crop data from FFmpeg, I.E. 720:360:0:58", type=int)

parser.add_argument("--time_scale", required=False, help="Optional - the multiplier to use on the subtitle timing.", type=float)
parser.add_argument("--time_offset", required=False, help="Optional - the this will shift the subtitle timing by the specified number of seconds.", type=float)

parser.add_argument("--resolution_scale", default=2, required=False, help="Optional - this value states how much to increase the SubStation Alpha resolution. All other items are scaled to match, so this will not make any visual changes.", type=int)

parser.add_argument("--line_height", default=32, required=False, help="Optional - this value is used to scale the subtitles by the average height of each line. Other factors, like the width and height, may force this value to be less than desired, to avoid truncating on the edges. Valid range from 10 to 120.", type=int)
parser.add_argument("--margin", default=8, required=False, help="Optional - this is how many pixels (Based on the original video resolution) to use as a margin on all four sides.", type=int)

parser.add_argument("--max_line_spacing", default=-1, required=False, help="Optional - this is how many rows of transparent pixels to render before stopping. This has the effect of bringing lines of text closer together. Use -1 to disable.", type=int)
parser.add_argument("--keep_position", default=True, required=False, help="Optional - this will allow subtitles to keep their original position, whether that be top, middle, bottom, left, center, or right.", type=bool)

parser.add_argument("--alpha_threshold", default=35, required=False, help="Optional - any alpha below this intensity will be considered transparent. Range is 0 to 255.", type=int)
parser.add_argument("--alignment_threshold", default=25, required=False, help="Optional - this value is a percentage used to determine the placement of a subtitle on the screen. Higher numbers mean subtitles are more likely to be at the vertical edges and horizontal center of the screen. Valid values are 0 to 100.", type=int)

parser.add_argument("--font_name", default="PixelCaption", required=False, help="Optional - the name of the font to use. Note that this IS NOT the file name, this is the name of the font when used in a word processor or other software!", type=str)

parser.add_argument("--shadow_size", default=1.25, required=False, help="Optional - this will add a 3D shadow effect to the resulting subtitles. Default value is 1, set to 0 to disable. Keep in mind that the subtitles are far more readable with the shadows on.", type=float)

parser.add_argument("--max_duration", default=10, required=False, help="Optional - this sets the maximum duration for subtitles. This may be important in cases where the duration is controlled by the timing on the next subtitle.", type=float)
parser.add_argument("--min_height", default=5, required=False, help="Optional - this sets the minimum height for a subtitle. Anything smaller than this will be ignored. This may be important in cases where the duration is controlled by the timing on the next subtitle. Set to 0 to use all subtitles.", type=int)
parser.add_argument("--min_width", default=5, required=False, help="Optional - this sets the minimum width for a subtitle. Anything smaller than this will be ignored. This may be important in cases where the duration is controlled by the timing on the next subtitle. Set to 0 to use all subtitles.", type=int)





args = parser.parse_args()

colorPalette = []
if args.palette != '':
	colorPalette = args.palette.split(',')
	if len(colorPalette) != 16:
		if args.convert_YUV == True:
			print(colors.red + 'Incorrect palette length. Must be 16 hexadecimal YUV colors!' + colors.none)
		else:
			print(colors.red + 'Incorrect palette length. Must be 16 hexadecimal RGB colors!' + colors.none)
		raise 
	for i in range(len(colorPalette)):
		colorPalette[i] = colorPalette[i].strip()
		colorPalette[i] = colorPalette[i].replace('"', '')
		colorPalette[i] = colorPalette[i].replace("'", '')
		if len(colorPalette[i]) != 6:
			errorMessage = 'Incorrect palette color length! Each color must be 6 hexadecimal RGB digits. Was given: ' + colorPalette[i]
			if args.convert_YUV == True:
				errorMessage = 'Incorrect palette color length! Each color must be 6 hexadecimal YUV digits. Was given: ' + colorPalette[i]
			print(colors.red + errorMessage + colors.none)
			raise Exception(errorMessage)
			exit()

cropData = ''
if not args.crop_data == None:
	cropData = args.crop_data

timeScale = 1
if not args.time_scale == None:
	timeScale = args.time_scale

timeOffset = 0
if not args.time_offset == None:
	timeOffset = args.time_offset

# This gives the subtitles a pleasant 3D look
shadowSize = args.shadow_size
shadowSize = max(0, shadowSize)


resolutionScale = args.resolution_scale		# This is used to increase the canvas size for better rendering

minMargin = args.margin * resolutionScale
fontHeight = args.line_height
fontHeight = clamp(fontHeight, 10, 120)

maxEmptyLines = args.max_line_spacing

keepPosition = args.keep_position

alphaThreshold = max(0, min(255, args.alpha_threshold))
alignmentThreshold = max(0, min(100, args.alignment_threshold)) / 100

fontName = args.font_name

use_sub_timestamps = args.use_sub_timestamps

printed = False


videoWidth = args.video_width


maxSubtitleDuration = args.max_duration
imageHeightThreshold = args.min_height
imageWidthThreshold = args.min_width


print()
print(colors.blue  + '---------------------------------------------------------------------')
print(colors.white + '                         Sub2ASS Version 1.0')
print(colors.blue  + '---------------------------------------------------------------------')
print(colors.green)
print('This library converts ' + colors.white + 'vobsub' + colors.green + '/' + colors.white + 'dvdsub' + colors.green + ' subtitles to SubStation Alpha.' + colors.yellow)

if fontName.lower() == 'pixelcaption':
	print('The use of this library REQUIRES a special font called PixelCaption.' + colors.none)
	print('The font is licensed as public domain, and should be included with')
	print('this project.')
else:
	print('The font has been overriden with: ' + colors.red + fontName)

print(colors.none)



extract_vob_sub_img_to_ass(args.input_file, args.output_file, args.video_width, args.video_height, colorPalette, cropData, timeScale, timeOffset)


