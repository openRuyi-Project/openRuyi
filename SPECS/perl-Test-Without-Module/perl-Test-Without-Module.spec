# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Without-Module
Version:        0.23
Release:        %autorelease
Summary:        Test fallback behaviour in absence of modules
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Test-Without-Module
#!RemoteAsset:  sha256:8289e1cd7f57017a816ab4127e29ecd7a754ae7cd5c037c41b3b3bf849c21d21
Source0:        https://www.cpan.org/authors/id/C/CO/CORION/Test-Without-Module-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)

%description
This module allows you to deliberately hide modules from a program even
though they are installed. This is mostly useful for testing modules that
have a fallback when a certain dependency module is not installed.

%files -f %{name}.files
%doc Changes README README.mkdn testrules.yml

%changelog
%autochangelog
