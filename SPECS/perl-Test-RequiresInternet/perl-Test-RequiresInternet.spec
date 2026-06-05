# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-RequiresInternet
Version:        0.05
Release:        %autorelease
Summary:        Test::RequiresInternet Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-RequiresInternet
#!RemoteAsset:  sha256:bba7b32a1cc0d58ce2ec20b200a7347c69631641e8cae8ff4567ad24ef1e833e
Source0:        https://www.cpan.org/authors/id/M/MA/MALLEN/Test-RequiresInternet-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
SYNOPSIS      use Test::More;      use Test::RequiresInternet
('www.example.com' => 80, 'foobar.io' => 25);

%files -f %{name}.files
%doc Changes README weaver.ini

%changelog
%autochangelog
