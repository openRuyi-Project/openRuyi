# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-MLDBM
Version:        2.05
Release:        %autorelease
Summary:        Store multi-level Perl hash structure in single level tied hash
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/MLDBM
#!RemoteAsset:  sha256:586880ed0c20801abbf6734747e13e0203edefece6ebc4f20ddb5059f02a17a2
Source0:        https://www.cpan.org/authors/id/C/CH/CHORNY/MLDBM-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.5.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper) >= 2.08
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)

Requires:       perl(Data::Dumper) >= 2.08

%description
This module can serve as a transparent interface to any TIEHASH package
that is required to store arbitrary perl data, including nested references.
Thus, this module can be used for storing references and other arbitrary
data within DBM databases.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
