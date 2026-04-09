# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Params-Util
Version:        1.102
Release:        %autorelease
Summary:        Simple, compact and correct param-checking functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Params-Util
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RE/REHSACK/Params-Util-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util) >= 1.18
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(XSLoader) >= 0.22

Requires:       perl(Scalar::Util) >= 1.18
Requires:       perl(XSLoader) >= 0.22

%description
Params::Util provides a basic set of importable functions that makes
checking parameters a hell of a lot easier

%prep
%setup -q -n Params-Util-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ARTISTIC-1.0 Changes GPL-1 README.md

%changelog
%autochangelog
