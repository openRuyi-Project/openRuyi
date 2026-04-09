# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-Remove
Version:        1.61
Release:        %autorelease
Summary:        Remove files and directories
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-Remove
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/File-Remove-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd) >= 3.29
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 3.29
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

Requires:       perl(Cwd) >= 3.29
Requires:       perl(File::Spec) >= 3.29

%description
File::Remove::remove removes files and directories. It acts like /bin/rm,
for the most part. Although unlink can be given a list of files, it will
not remove directories; this module remedies that. It also accepts
wildcards, * and ?, as arguments for filenames.

%prep
%setup -q -n File-Remove-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README scripts weaver.ini

%changelog
%autochangelog
