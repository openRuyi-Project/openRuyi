# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-YAML-LibYAML
Version:        0.904.0
Release:        %autorelease
Summary:        YAML::LibYAML Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/YAML-LibYAML
#!RemoteAsset:  sha256:b656b0b11a4219c125679e8cbf7436a3f636e833fd63cf322d171dcb7c3eaf3e
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-LibYAML-v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.9
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%description
use YAML::XS;

# Classic functional interface
my $yaml = Dump [ 1..4 ]; my $array = Load $yaml;

# EXPERIMENTAL: Object Oriented interface for YAML 1.2 Incompatible to
# functional interface!
my $xs = YAML::XS->new; my $yaml = $xs->dump([ 1..4 ]); my $array = $xs-
>load($yaml);

%prep
%setup -q -n YAML-LibYAML-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%files -f %{name}.files
%doc CONTRIBUTING.md Changes LibYAML README
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/YAML*

%changelog
%autochangelog
