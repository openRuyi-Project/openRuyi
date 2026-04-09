# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Perl-Tidy
Version:        20250912
Release:        %autorelease
Summary:        Parses and beautifies perl source
License:        GPL-1.0-or-later
URL:            https://metacpan.org/dist/Perl-Tidy
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/S/SH/SHANCOCK/Perl-Tidy-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module makes the functionality of the perltidy utility available to
perl scripts. Any or all of the input parameters may be omitted, in which
case the @ARGV array will be used to provide input parameters as described
in the perltidy(1) man page.

%prep
%setup -q -n Perl-Tidy-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc BUGS.md CHANGES.md INSTALL.md pm2pl README.md SECURITY.md

%changelog
%autochangelog
