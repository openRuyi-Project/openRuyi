# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Pod
Version:        1.52
Release:        %autorelease
Summary:        Check for POD errors in files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Pod
#!RemoteAsset:  sha256:60a8dbcc60168bf1daa5cc2350236df9343e9878f4ab9830970a5dde6fe8e5fc
Source0:        https://www.cpan.org/authors/id/E/ET/ETHER/Test-Pod-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Pod::Simple) >= 3.05
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::More) >= 0.62

Requires:       perl(Pod::Simple) >= 3.05
Requires:       perl(Test::Builder::Tester) >= 1.02
Requires:       perl(Test::More) >= 0.62

%description
Check POD files for errors or warnings in a test file, using Pod::Simple to
do the heavy lifting.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
