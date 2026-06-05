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
#!RemoteAsset:  sha256:05c29ec3482e572313a60da2181b0b30c5db7cf01f8ae7616ad67e1b66263296
Source0:        https://www.cpan.org/authors/id/D/DC/DCONWAY/Lingua-EN-Inflect-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
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

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
