# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-link-presentation
%global full_version 0.2.2
%global pkgname objc2-link-presentation-0.2

Name:           rust-objc2-link-presentation-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "objc2-link-presentation"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:a1a1ae721c5e35be65f01a03b6d2ac13a54cb4fa70d8a5da293d7b0020261398
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Requires:       crate(objc2-foundation-0.2) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/lpfoundation) = %{version}

%description
Source code for takopackized Rust crate "objc2-link-presentation"

%package     -n %{name}+lperror
Summary:        Bindings to the LinkPresentation framework - feature "LPError"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/lperror) = %{version}

%description -n %{name}+lperror
This metapackage enables feature "LPError" for the Rust objc2-link-presentation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lplinkmetadata
Summary:        Bindings to the LinkPresentation framework - feature "LPLinkMetadata"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsitemprovider) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/lplinkmetadata) = %{version}

%description -n %{name}+lplinkmetadata
This metapackage enables feature "LPLinkMetadata" for the Rust objc2-link-presentation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lplinkview
Summary:        Bindings to the LinkPresentation framework - feature "LPLinkView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-app-kit-0.2/nsaccessibilityprotocols) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsanimation) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsappearance) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsdragging) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsresponder) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsuserinterfaceitemidentification) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsview) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/lplinkview) = %{version}

%description -n %{name}+lplinkview
This metapackage enables feature "LPLinkView" for the Rust objc2-link-presentation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lpmetadataprovider
Summary:        Bindings to the LinkPresentation framework - feature "LPMetadataProvider"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurlrequest) >= 0.2.2
Provides:       crate(%{pkgname}/lpmetadataprovider) = %{version}

%description -n %{name}+lpmetadataprovider
This metapackage enables feature "LPMetadataProvider" for the Rust objc2-link-presentation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Bindings to the LinkPresentation framework - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/lperror) = %{version}
Requires:       crate(%{pkgname}/lpfoundation) = %{version}
Requires:       crate(%{pkgname}/lplinkmetadata) = %{version}
Requires:       crate(%{pkgname}/lplinkview) = %{version}
Requires:       crate(%{pkgname}/lpmetadataprovider) = %{version}
Requires:       crate(%{pkgname}/objc2-app-kit) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust objc2-link-presentation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Bindings to the LinkPresentation framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/alloc) >= 0.5.1
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Requires:       crate(objc2-app-kit-0.2/alloc) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/alloc) >= 0.2.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2-link-presentation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the LinkPresentation framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5) >= 0.5.1
Requires:       crate(objc2-app-kit-0.2/block2) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/block2) >= 0.2.2
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-link-presentation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-app-kit
Summary:        Bindings to the LinkPresentation framework - feature "objc2-app-kit"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-app-kit-0.2) >= 0.2.2
Provides:       crate(%{pkgname}/objc2-app-kit) = %{version}

%description -n %{name}+objc2-app-kit
This metapackage enables feature "objc2-app-kit" for the Rust objc2-link-presentation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings to the LinkPresentation framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(block2-0.5/std) >= 0.5.1
Requires:       crate(objc2-0.5/std) >= 0.5.2
Requires:       crate(objc2-app-kit-0.2/std) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/std) >= 0.2.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2-link-presentation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
