# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Time-HiRes
Version:        1.9764
Release:        %autorelease
Summary:        High resolution alarm, sleep, gettimeofday, interval timers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Time-HiRes
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/A/AT/ATOOMIC/Time-HiRes-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)

%description
The Time::HiRes module implements a Perl interface to the usleep,
nanosleep, ualarm, gettimeofday, and setitimer/getitimer system calls, in
other words, high resolution time and timers. See the "EXAMPLES" section
below and the test scripts for usage; see your system documentation for the
description of the underlying nanosleep or usleep, ualarm, gettimeofday,
and setitimer/getitimer calls.

%prep
%setup -q -n Time-HiRes-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README TODO

%changelog
%autochangelog
