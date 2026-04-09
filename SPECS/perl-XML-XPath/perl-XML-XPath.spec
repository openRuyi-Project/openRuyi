# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XML-XPath
Version:        1.48
Release:        %autorelease
Summary:        Parse and evaluate XPath statements
License:        Artistic-2.0
URL:            https://metacpan.org/dist/XML-XPath
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/M/MA/MANWAR/XML-XPath-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Path::Tiny) >= 0.076
BuildRequires:  perl(Scalar::Util) >= 1.45
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::Parser) >= 2.23

Requires:       perl(Scalar::Util) >= 1.45
Requires:       perl(XML::Parser) >= 2.23

%description
This module aims to comply exactly to the XPath specification at
http://www.w3.org/TR/xpath and yet allow extensions to be added in the form
of functions.Modules such as XSLT and XPointer may need to do this as they
support functionality beyond XPath.

%prep
%setup -q -n XML-XPath-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README TODO

%changelog
%autochangelog
