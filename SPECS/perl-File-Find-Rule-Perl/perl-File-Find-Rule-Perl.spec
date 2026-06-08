# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-Find-Rule-Perl
Version:        1.16
Release:        %autorelease
Summary:        Common rules for searching for Perl things
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-Find-Rule-Perl
#!RemoteAsset:  sha256:ae1886050d9ca21223c073e2870abdc80dc30e3f55289a11c37da3820a8321ff
Source0:        https://www.cpan.org/authors/id/E/ET/ETHER/File-Find-Rule-Perl-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule) >= 0.20
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(Params::Util) >= 0.38
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.38
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Number::Compare)

Requires:       perl(File::Find::Rule) >= 0.20
Requires:       perl(File::Spec) >= 0.82
Requires:       perl(Params::Util) >= 0.38
Requires:       perl(Parse::CPAN::Meta) >= 1.38

%description
I write a lot of things that muck with Perl files. And it always annoyed
me that finding "perl files" requires a moderately complex
File::Find::Rule pattern.

%check
# RPM packaging helpers leave generated file-list artifacts in the build
# directory, which breaks t/03_no_index.t file list expectations.
rm -f debug*.list elfbins.list

if [ -f %{name}.files ]; then
    mv %{name}.files ../%{name}.files.rpmbuild
fi

%{make_build} test

if [ -f ../%{name}.files.rpmbuild ]; then
    mv ../%{name}.files.rpmbuild %{name}.files
fi

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog
