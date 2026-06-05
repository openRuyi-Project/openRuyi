# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XML-Simple
Version:        2.25
Release:        %autorelease
Summary:        API for simple XML files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XML-Simple
#!RemoteAsset:  sha256:531fddaebea2416743eb5c4fdfab028f502123d9a220405a4100e68fc480dbf8
Source0:        https://www.cpan.org/authors/id/G/GR/GRANTM/XML-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(XML::NamespaceSupport) >= 1.04
BuildRequires:  perl(XML::SAX) >= 0.15
BuildRequires:  perl(XML::SAX::Expat)

Requires:       perl(XML::NamespaceSupport) >= 1.04
Requires:       perl(XML::SAX) >= 0.15

%description
The XML::Simple module provides a simple API layer on top of an underlying
XML parsing module (either XML::Parser or one of the SAX2 parser modules).
Two functions are exported: XMLin() and XMLout(). Note: you can explicitly
request the lower case versions of the function names: xml_in() and
xml_out().

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
