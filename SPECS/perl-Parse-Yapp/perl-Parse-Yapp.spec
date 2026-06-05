# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Parse-Yapp
Version:        1.21
Release:        %autorelease
Summary:        Perl extension for generating and using LALR parsers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Parse-Yapp
#!RemoteAsset:  sha256:3810e998308fba2e0f4f26043035032b027ce51ce5c8a52a8b8e340ca65f13e5
Source0:        https://www.cpan.org/authors/id/W/WB/WBRASWELL/Parse-Yapp-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Parse::Yapp (Yet Another Perl Parser compiler) is a collection of modules
that let you generate and use yacc like thread safe (reentrant) parsers
with perl object oriented interface.

%files -f %{name}.files
%doc Calc.yp Changes README README.md yapp YappParse.yp

%changelog
%autochangelog
