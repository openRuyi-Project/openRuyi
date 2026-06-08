# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Socket
Version:        2.041
Release:        %autorelease
Summary:        Networking constants and support functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Socket
#!RemoteAsset:  sha256:91f57ca9e5fcc5c7ce08e52e73841afafc56a688514d9d8b815cabe14a95b556
Source0:        https://www.cpan.org/authors/id/P/PE/PEVANS/Socket-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel

%description
This module provides a variety of constants, structure manipulators and
other functions related to socket-based networking. The values and
functions provided are useful when used in conjunction with Perl core
functions such as socket(), setsockopt() and bind(). It also provides
several other support functions, mostly for dealing with conversions of
network addresses between human-readable and native binary forms, and for
hostname resolver operations.

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog
