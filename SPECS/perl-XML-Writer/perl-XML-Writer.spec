# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XML-Writer
Version:        0.900
Release:        %autorelease
Summary:        Perl extension for writing XML documents
License:        MIT
URL:            https://metacpan.org/dist/XML-Writer
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/J/JO/JOSEPHW/XML-Writer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.047

%description
XML::Writer is a helper module for Perl programs that write an XML
document. The module handles all escaping for attribute values and
character data and constructs different types of markup, such as tags,
comments, and processing instructions.

%prep
%setup -q -n XML-Writer-%{version}

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
