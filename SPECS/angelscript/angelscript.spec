# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           angelscript
Version:        2.38.0
Release:        %autorelease
Summary:        A cross-platform scripting library
License:        zlib
URL:            https://www.angelcode.com/angelscript
VCS:            git:https://github.com/anjo76/angelscript
#!RemoteAsset:  sha256:b33b5dbcda10317ef67d628353d83246984ce6fcac102d4dc2aed121eba52e6f
Source:         https://www.angelcode.com/angelscript/sdk/files/angelscript_%{version}.zip
BuildSystem:    cmake

Patch2000:      2000-install-libraries-and-CMake-files-to-GNUInstallDirs.patch

BuildOption(conf):  -S angelscript/projects/cmake
BuildOption(conf):  -DBUILD_SHARED_LIBS:BOOL=ON

BuildRequires:  cmake
BuildRequires:  unzip
BuildRequires:  dos2unix

%description
The AngelCode Scripting Library, or AngelScript as it is also known,
is an extremely flexible cross-platform scripting library designed to
allow applications to extend their functionality through external scripts.
It has been designed from the beginning to be an easy to use component,
both for the application programmer and the script writer.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n sdk
# Normalize mixed CRLF/LF line endings before applying the GNUInstallDirs patch.
dos2unix angelscript/projects/cmake/CMakeLists.txt
%patch 2000 -p1

%files
%doc docs/articles/*.html
%license docs/manual/doc_license.html
%{_libdir}/libangelscript.so.*

%files devel
%doc docs/manual/*
%{_libdir}/libangelscript.so
%{_includedir}/angelscript.h
%dir %{_libdir}/cmake/Angelscript
%{_libdir}/cmake/Angelscript/*.cmake

%changelog
%autochangelog
