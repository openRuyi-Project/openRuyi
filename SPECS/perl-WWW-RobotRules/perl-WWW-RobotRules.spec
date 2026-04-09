# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-WWW-RobotRules
Version:        6.02
Release:        %autorelease
Summary:        Database of robots.txt-derived permissions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/WWW-RobotRules
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/WWW-RobotRules-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(AnyDBM_File)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(URI) >= 1.10

Requires:       perl(URI) >= 1.10

%description
This module parses /robots.txt files as specified in "A Standard for Robot
Exclusion", at <http://www.robotstxt.org/wc/norobots.html> Webmasters can
use the /robots.txt file to forbid conforming robots from accessing parts
of their web site.

%prep
%setup -q -n WWW-RobotRules-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
