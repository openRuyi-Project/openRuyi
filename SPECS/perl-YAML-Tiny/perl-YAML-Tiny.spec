# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-YAML-Tiny
Version:        1.76
Release:        %autorelease
Summary:        Read/Write YAML files with as little code as possible
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/YAML-Tiny
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/YAML-Tiny-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(open)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
YAML::Tiny is a perl class for reading and writing YAML-style files,
written with as little code as possible, reducing load time and
memory overhead.

%prep
%setup -q -n YAML-Tiny-%{version}

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
