# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Mock-Config
Version:        0.05
Release:        %autorelease
Summary:        Mock::Config Perl module
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Mock-Config
#!RemoteAsset:  sha256:20017096c6464fbd59ae7549fbc663bfb0c9014d7ac3a457a81a7e408268f62c
Source0:        https://www.cpan.org/authors/id/R/RU/RURBAN/Mock-Config-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
use Mock::Config; Mock::Config->import(startperl => ''); print
$Config{startperl}, ' mocked to empty'; Mock::Config->unimport;

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
