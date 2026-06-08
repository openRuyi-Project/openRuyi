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
#!RemoteAsset:  sha256:9841be5587bfb7cd1f2fe267b5e5ac04ce25e79d5cc77e5ef9a9c5abd101d7b1
Source0:        https://www.cpan.org/authors/id/A/AT/ATOOMIC/Time-HiRes-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
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
BuildRequires:  perl-devel

%description
The Time::HiRes module implements a Perl interface to the usleep,
nanosleep, ualarm, gettimeofday, and setitimer/getitimer system calls, in
other words, high resolution time and timers. See the "EXAMPLES" section
below and the test scripts for usage; see your system documentation for the
description of the underlying nanosleep or usleep, ualarm, gettimeofday,
and setitimer/getitimer calls.

%files -f %{name}.files
%doc Changes README TODO

%changelog
%autochangelog
