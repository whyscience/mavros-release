Name:           ros-indigo-mavros
Version:        0.15.0
Release:        0%{?dist}
Summary:        ROS mavros package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       eigen3-devel
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-eigen-conversions
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-libmavconn
Requires:       ros-indigo-mavlink
Requires:       ros-indigo-mavros-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-rosconsole-bridge
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf2-ros
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-eigen-conversions
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-libmavconn
BuildRequires:  ros-indigo-mavlink
BuildRequires:  ros-indigo-mavros-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-rosconsole-bridge
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf2-ros

%description
MAVROS -- MAVLink extendable communication node for ROS with proxy for Ground
Control Station.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Sep 17 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.15.0-0
- Autogenerated by Bloom

* Thu Aug 20 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.14.2-0
- Autogenerated by Bloom

* Wed Aug 19 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.14.1-0
- Autogenerated by Bloom

* Mon Aug 17 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.14.0-0
- Autogenerated by Bloom

* Wed Aug 05 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.13.1-0
- Autogenerated by Bloom

* Sat Aug 01 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.13.0-0
- Autogenerated by Bloom

* Wed Jul 01 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.12.0-0
- Autogenerated by Bloom

* Sun Apr 26 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.2-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.1-0
- Autogenerated by Bloom

* Tue Mar 24 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.0-0
- Autogenerated by Bloom

* Wed Feb 25 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.10.2-0
- Autogenerated by Bloom

* Mon Feb 02 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.10.1-0
- Autogenerated by Bloom

* Sat Jan 24 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.10.0-0
- Autogenerated by Bloom

* Tue Jan 06 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.9.4-0
- Autogenerated by Bloom

* Tue Dec 30 2014 Vladimir Ermakov <vooon341@gmail.com> - 0.9.3-0
- Autogenerated by Bloom

