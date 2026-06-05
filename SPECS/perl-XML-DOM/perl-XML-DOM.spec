# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XML-DOM
Version:        1.46
Release:        %autorelease
Summary:        Perl module for building DOM Level 1 compliant document structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XML-DOM
#!RemoteAsset:  sha256:8ba24b0b459b01d6c5e5b0408829c7d5dfe47ff79b3548c813759048099b175e
Source0:        https://www.cpan.org/authors/id/T/TJ/TJMATHER/XML-DOM-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(XML::Parser) >= 2.30
BuildRequires:  perl(XML::Parser::PerlSAX) >= 0.07
BuildRequires:  perl(XML::RegExp)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(File::ShareDir)

Requires:       perl(XML::Parser) >= 2.30
Requires:       perl(XML::Parser::PerlSAX) >= 0.07

%description
This module extends the XML::Parser module by Clark Cooper. The XML::Parser
module is built on top of XML::Parser::Expat, which is a lower level
interface to James Clark's expat library.

%files -f %{name}.files
%doc BUGS Changes FAQ.xml README XML-Parser-2.31.patch

%changelog
%autochangelog
