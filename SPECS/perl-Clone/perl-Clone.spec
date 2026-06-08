# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Clone
Version:        0.50
Release:        %autorelease
Summary:        Recursively copy Perl datatypes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Clone
#!RemoteAsset:  sha256:f9732a4a857974db30905233589113003301b585b0cecda29a21cfba5bb014f9
Source0:        https://www.cpan.org/authors/id/A/AT/ATOOMIC/Clone-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(B::COW) >= 0.004
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl-devel

%description
This module provides a clone() method which makes recursive copies of
nested hash, array, scalar and reference types, including tied variables
and objects.

%files -f %{name}.files
%doc AI_POLICY.md Changes README.md SECURITY.md

%changelog
%autochangelog
