# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XML-TokeParser
Version:        0.05
Release:        %autorelease
Summary:        Simplified interface to XML::Parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XML-TokeParser
#!RemoteAsset:  sha256:8539b4f98436b1a6d088341a8b4530b7922acd651f3f29377f8b1948c7e2d7c2
Source0:        https://cpan.metacpan.org/authors/id/P/PO/PODMASTER/XML-TokeParser-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(XML::Parser) >= 2

Requires:       perl(XML::Parser) >= 2

%description
XML::TokeParser provides a token oriented interface built on top of
XML::Parser.

%files -f %{name}.files
%doc Changes README TODO TokeParser.xml

%changelog
%autochangelog
