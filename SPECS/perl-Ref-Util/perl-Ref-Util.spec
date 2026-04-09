# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Ref-Util
Version:        0.204
Release:        %autorelease
Summary:        Utility functions for checking references
License:        MIT
URL:            https://metacpan.org/dist/Ref-Util
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/A/AR/ARC/Ref-Util-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96

Requires:       perl(Exporter) >= 5.57

%description
Ref::Util introduces several functions to help identify references in a
smarter (and usually faster) way. In short:

%prep
%setup -q -n Ref-Util-%{version}

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
