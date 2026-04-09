# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Config-AutoConf
Version:        0.320
Release:        %autorelease
Summary:        Module to implement some of AutoConf macros in pure perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Config-AutoConf
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/A/AM/AMBS/Config-AutoConf-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.23
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util) >= 1.18
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.9
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(warnings)

Requires:       perl(ExtUtils::CBuilder) >= 0.280220
Requires:       perl(Scalar::Util) >= 1.18

%description
Config::AutoConf is intended to provide the same opportunities to Perl
developers as GNU Autoconf does for Shell developers.

%prep
%setup -q -n Config-AutoConf-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ARTISTIC-1.0 Changes GPL-1 README.md testTc852_

%changelog
%autochangelog
