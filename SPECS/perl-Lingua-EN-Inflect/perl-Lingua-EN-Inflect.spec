# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Lingua-EN-Inflect
Version:        1.905
Release:        %autorelease
Summary:        Convert singular to plural. Select "a" or "an"
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Lingua-EN-Inflect
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DC/DCONWAY/Lingua-EN-Inflect-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
[Note: This module is strictly in maintenance mode now. Take a look at the
newer Lingua::EN::Inflexion module, which offers a cleaner and more
convenient interface, has many more features (including plural->singular
inflexions), and is also much better tested. If you have existing code that
relies on Lingua::EN::Inflect, see the section of the documentation
entitled "CONVERTING FROM LINGUA::EN::INFLECT". ]

%prep
%setup -q -n Lingua-EN-Inflect-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
