# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-HTML-Form
Version:        6.13
Release:        %autorelease
Summary:        Class that represents an HTML form element
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTML-Form
#!RemoteAsset:  sha256:ae5ad0f6fe70b1a382789d5e83a9b669cc541ee9d459e1bfa89b43ae0c014cdd
Source0:        https://www.cpan.org/authors/id/O/OA/OALDERS/HTML-Form-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 2
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTTP::Request) >= 7.01
BuildRequires:  perl(HTTP::Request::Common) >= 6.03
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(URI) >= 1.10
BuildRequires:  perl(warnings)
BuildRequires:  perl(HTML::Tagset)

Requires:       perl(Encode) >= 2
Requires:       perl(HTTP::Request) >= 7.01
Requires:       perl(HTTP::Request::Common) >= 6.03
Requires:       perl(Test::More) >= 0.96
Requires:       perl(URI) >= 1.10

%description
Objects of the HTML::Form class represents a single HTML <form> ... </form>
instance. A form consists of a sequence of inputs that usually have names,
and which can take on various values. The state of a form can be tweaked
and it can then be asked to provide HTTP::Request objects that can be
passed to the request() method of LWP::UserAgent.

%files -f %{name}.files
%doc Changes perltidyrc

%changelog
%autochangelog
