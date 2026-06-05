# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-WWW-RobotRules
Version:        6.03
Release:        %autorelease
Summary:        Database of robots.txt-derived permissions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/WWW-RobotRules
#!RemoteAsset:  sha256:8522b532935a11bfa688c2e113bac66729df4851be50c2c26d4b06f45fade472
Source0:        https://www.cpan.org/authors/id/O/OA/OALDERS/WWW-RobotRules-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(AnyDBM_File)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(URI) >= 1.10
BuildRequires:  perl(warnings)

Requires:       perl(URI) >= 1.10

%description
This module parses /robots.txt files as specified in at
https://www.robotstxt.org/robotstxt.html. Webmasters can use the
/robots.txt file to forbid conforming robots from accessing parts of
their web site.

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog
