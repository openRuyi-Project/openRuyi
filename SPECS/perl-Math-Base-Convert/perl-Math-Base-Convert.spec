# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Math-Base-Convert
Version:        0.13
Release:        %autorelease
Summary:        Very fast base to base conversion
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Math-Base-Convert
#!RemoteAsset:  sha256:289c0c33bc9886db3dc2cf949d8e0ab24e36c67b9e833355941d70aaf3519ed2
Source0:        https://www.cpan.org/authors/id/M/MI/MIKER/Math-Base-Convert-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module provides fast functions and methods to convert between
arbitrary number bases from 2 (binary) thru 65535.

%files -f %{name}.files
%doc bitmaps Changes README recurse2txt

%changelog
%autochangelog
