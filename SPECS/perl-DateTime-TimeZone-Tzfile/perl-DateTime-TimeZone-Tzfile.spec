# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DateTime-TimeZone-Tzfile
Version:        0.011
Release:        %autorelease
Summary:        Tzfile (zoneinfo) timezone files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DateTime-TimeZone-Tzfile
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/DateTime-TimeZone-Tzfile-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::ISO8601)
BuildRequires:  perl(DateTime::TimeZone::SystemV) >= 0.009
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::File) >= 1.13
BuildRequires:  perl(IO::Handle) >= 1.08
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

Requires:       perl(DateTime::TimeZone::SystemV) >= 0.009
Requires:       perl(IO::File) >= 1.13
Requires:       perl(IO::Handle) >= 1.08

%description
An instance of this class represents a timezone that was encoded in a file
in the tzfile(5) format. These can express arbitrary patterns of offsets
from Universal Time, changing over time. Offsets and change times are
limited to a resolution of one second.

%prep
%setup -q -n DateTime-TimeZone-Tzfile-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
