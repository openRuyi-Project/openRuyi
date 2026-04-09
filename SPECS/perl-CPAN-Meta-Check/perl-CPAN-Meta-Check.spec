# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-CPAN-Meta-Check
Version:        0.018
Release:        %autorelease
Summary:        Verify requirements in a CPAN::Meta object
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/CPAN-Meta-Check
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/CPAN-Meta-Check-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(base)
BuildRequires:  perl(CPAN::Meta) >= 2.120920
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.132830
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Metadata) >= 1.000023
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)

Requires:       perl(CPAN::Meta::Prereqs) >= 2.132830
Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(Module::Metadata) >= 1.000023

%description
This module verifies if requirements described in a CPAN::Meta object
are present.

%prep
%setup -q -n CPAN-Meta-Check-%{version}

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
