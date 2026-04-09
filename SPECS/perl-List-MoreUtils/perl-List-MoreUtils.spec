# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-List-MoreUtils
Version:        0.430
Release:        %autorelease
Summary:        Provide the stuff missing in List::Util
License:        Apache-2.0
URL:            https://metacpan.org/dist/List-MoreUtils
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter::Tiny) >= 0.038
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::MoreUtils::XS) >= 0.430
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.96

Requires:       perl(Exporter::Tiny) >= 0.038
Requires:       perl(List::MoreUtils::XS) >= 0.430

%description
List::MoreUtils provides some trivial but commonly needed functionality on
lists which is not going to go into List::Util.

%prep
%setup -q -n List-MoreUtils-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ARTISTIC-1.0 Changes GPL-1 README.md

%changelog
%autochangelog
