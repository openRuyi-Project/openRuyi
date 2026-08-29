# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Date-ISO8601
Version:        0.005
Release:        %autorelease
Summary:        Three ISO 8601 numerical calendars
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Date-ISO8601
#!RemoteAsset:  sha256:84bef53cc808bd11830fbb434c9836c3dc4b24a58db878f5073db198fb9a586c
Source0:        https://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Date-ISO8601-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
The international standard ISO 8601 "Data elements and interchange formats
- Information interchange - Representation of dates and times" defines
three distinct calendars by which days can be labelled. It also defines
textual formats for the representation of dates in these calendars. This
module provides functions to convert dates between these three calendars
and Chronological Julian Day Numbers, which is a suitable format to do
arithmetic with. It also supplies functions that describe the shape of
these calendars, to assist in calendrical calculations. It also supplies
functions to represent dates textually in the ISO 8601 formats. ISO 8601
also covers time of day and time periods, but this module does nothing
relating to those parts of the standard; this is only about labelling days.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
