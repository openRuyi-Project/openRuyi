# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Term-ANSIColor
Version:        5.01
Release:        %autorelease
Summary:        Color screen output using ANSI escape sequences
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Term-ANSIColor
#!RemoteAsset:  sha256:6281bd87cced7a885c38aa104498e3cd4b5f4c276087442cf68c67379318f27d
Source0:        https://www.cpan.org/authors/id/R/RR/RRA/Term-ANSIColor-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module has two interfaces, one through color() and colored() and the
other through constants. It also offers the utility functions uncolor(),
colorstrip(), colorvalid(), and coloralias(), which have to be explicitly
imported to be used (see "SYNOPSIS").

%files -f %{name}.files
%doc Changes README README.md THANKS TODO

%changelog
%autochangelog
