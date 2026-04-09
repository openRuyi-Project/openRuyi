# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Requires
Version:        0.11
Release:        %autorelease
Summary:        Checks to see if the module can be loaded
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Requires
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/T/TO/TOKUHIROM/Test-Requires-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More) >= 0.47

Requires:       perl(Test::More) >= 0.47

%description
Test::Requires checks to see if the module can be loaded.

%prep
%setup -q -n Test-Requires-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes minil.toml README.md

%changelog
%autochangelog
