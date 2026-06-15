# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XML-Descent
Version:        1.04
Release:        %autorelease
Summary:        Recursive descent XML parsing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XML-Descent
#!RemoteAsset:  sha256:a711b856f8cdf5e647a44c71f967d48c096035b9dbd3f1efbdbea40605afbd50
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDYA/XML-Descent-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::TokeParser)

Requires:       perl(XML::TokeParser)

%description
XML::Descent implements recursive descent XML parsing for applications that
want structured callbacks over XML tokens.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
