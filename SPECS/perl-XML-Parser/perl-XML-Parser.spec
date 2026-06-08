# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XML-Parser
Version:        2.59
Release:        %autorelease
Summary:        Perl module for parsing XML documents
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XML-Parser
#!RemoteAsset:  sha256:a358fd7c49f5e27717a644a9102bd21dc7fc25a415983279c59b1580e2b62a58
Source0:        https://www.cpan.org/authors/id/T/TO/TODDR/XML-Parser-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(expat)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(File::ShareDir::Install)

%description
This module provides ways to parse XML documents. It is built on top of
XML::Parser::Expat, which is a lower level interface to James Clark's expat
library. Each call to one of the parsing methods creates a new instance of
XML::Parser::Expat which is then used to parse the document. Expat options
may be provided when the XML::Parser object is created. These options are
then passed on to the Expat object on each parse call. They can also be
given as extra arguments to the parse methods, in which case they override
options given at XML::Parser creation time.

%files -f %{name}.files
%doc AI_POLICY.md Changes CONTRIBUTING.md Expat Parser README.md samples SECURITY.md share

%changelog
%autochangelog
