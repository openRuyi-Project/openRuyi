# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Config-Tiny
Version:        2.30
Release:        %autorelease
Summary:        Read/Write .ini style files with as little code as possible
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Config-Tiny
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RS/RSAVAGE/Config-Tiny-%{version}.tgz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 3.30
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 1.001002
BuildRequires:  perl(utf8)

Requires:       perl(File::Spec) >= 3.30
Requires:       perl(File::Temp) >= 0.22

%description
Config::Tiny is a Perl class to read and write .ini style
configuration files with as little code as possible, reducing load
time and memory overhead.

%prep
%setup -q -n Config-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changelog.ini Changes README

%changelog
%autochangelog
