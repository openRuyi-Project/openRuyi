# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-ParseWords
Version:        3.31
Release:        %autorelease
Summary:        Parse text into an array of tokens or array of arrays
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-ParseWords
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/N/NE/NEILB/Text-ParseWords-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)

%description
The nested_quotewords() and quotewords() functions accept a delimiter
(which can be a regular expression) and a list of lines and then breaks
those lines up into a list of words ignoring delimiters that appear
inside quotes. quotewords() returns all of the tokens in a single long
list, while nested_quotewords() returns a list of token lists
corresponding to the elements of @lines. parse_line() does tokenizing on
a single string. The *quotewords() functions simply call parse_line(), so
if you're only splitting one line you can call parse_line() directly and
save a function call.

%prep
%setup -q -n Text-ParseWords-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES README

%changelog
%autochangelog
