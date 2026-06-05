# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Module-Runtime
Version:        0.018
Release:        %autorelease
Summary:        Runtime module handling
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-Runtime
#!RemoteAsset:  sha256:0bf77ef68e53721914ff554eada20973596310b4e2cf1401fc958601807de577
Source0:        https://www.cpan.org/authors/id/H/HA/HAARG/Module-Runtime-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
The functions exported by this module deal with runtime handling of Perl
modules, which are normally handled at compile time. This module avoids
using any other modules, so that it can be used in low-level
infrastructure.

%files -f %{name}.files
%doc Changes prereqs.yml README TODO weaver.ini

%changelog
%autochangelog
