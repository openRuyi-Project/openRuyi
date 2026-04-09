# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Date-Manip
Version:        6.98
Release:        %autorelease
Summary:        Date manipulation routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Date-Manip
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/S/SB/SBECK/Date-Manip-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Inter) >= 1.09
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)

%description
Date::Manip is a series of modules designed to make any common date/time
operation easy to do. Operations such as comparing two times, determining a
date a given amount of time from another, or parsing international times
are all easily done. It deals with time as it is used in the Gregorian
calendar (the one currently in use) with full support for time changes due
to daylight saving time.

%prep
%setup -q -n Date-Manip-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README README.first

%changelog
%autochangelog
