# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Readonly
Version:        2.05
Release:        %autorelease
Summary:        Readonly Perl module
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Readonly
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/S/SA/SANKO/Readonly-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.5.0
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Module::Build::Tiny)

%description
# Deep Read-only scalar
Readonly::Scalar    $sca => $initial_value; Readonly::Scalar my $sca =>
$initial_value;

%prep
%setup -q -n Readonly-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes minil.toml README.md

%changelog
%autochangelog
