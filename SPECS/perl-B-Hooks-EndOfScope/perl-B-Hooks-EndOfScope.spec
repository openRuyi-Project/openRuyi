# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-B-Hooks-EndOfScope
Version:        0.28
Release:        %autorelease
Summary:        Execute code after a scope finished compilation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/B-Hooks-EndOfScope
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/B-Hooks-EndOfScope-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Implementation) >= 0.05
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001006
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)

Requires:       perl(Module::Implementation) >= 0.05
Requires:       perl(Sub::Exporter::Progressive) >= 0.001006

%description
This module allows you to execute code when perl finished compiling the
surrounding scope.

%prep
%setup -q -n B-Hooks-EndOfScope-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README

%changelog
%autochangelog
