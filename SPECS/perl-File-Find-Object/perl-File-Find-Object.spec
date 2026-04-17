# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-Find-Object
Version:        0.3.9
Release:        %autorelease
Summary:        Object oriented File::Find replacement
License:        Artistic-2.0
URL:            https://metacpan.org/dist/File-Find-Object
#!RemoteAsset:  sha256:7e99afe4a9d992fcef1dfea42e1f95475706aed94f185068a89f729b512735f8
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/File-Find-Object-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::TreeCreate)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::File) >= 1.993
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
File::Find::Object does the same job as File::Find but works like an object
and with an iterator. As File::Find is not object oriented, one cannot
perform multiple searches in the same application. The second problem of
File::Find is its file processing: after starting its main loop, one cannot
easily wait for another event and so get the next result.

%prep
%setup -q -n File-Find-Object-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --installdirs=vendor --destdir=%{buildroot}
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md examples scripts weaver.ini
%license LICENSE

%changelog
%autochangelog
