# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-HTML-Form
Version:        6.12
Release:        %autorelease
Summary:        Class that represents an HTML form element
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTML-Form
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/O/OA/OALDERS/HTML-Form-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 2
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTTP::Request) >= 6
BuildRequires:  perl(HTTP::Request::Common) >= 6.03
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(URI) >= 1.10
BuildRequires:  perl(warnings)

Requires:       perl(Encode) >= 2
Requires:       perl(HTTP::Request) >= 6
Requires:       perl(HTTP::Request::Common) >= 6.03
Requires:       perl(Test::More) >= 0.96
Requires:       perl(URI) >= 1.10

%description
Objects of the HTML::Form class represents a single HTML <form> ... </form>
instance. A form consists of a sequence of inputs that usually have names,
and which can take on various values. The state of a form can be tweaked
and it can then be asked to provide HTTP::Request objects that can be
passed to the request() method of LWP::UserAgent.

%prep
%setup -q -n HTML-Form-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes perltidyrc

%changelog
%autochangelog
